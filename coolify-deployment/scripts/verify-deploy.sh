#!/usr/bin/env bash
# Poll a live URL until a Coolify deploy lands, then prove the served bytes match
# the repo. "Merged" is not "deployed" and "deployed" is not "correct".
#
#   verify-deploy.sh <url> [repo-file] [max-minutes]
#
#   verify-deploy.sh https://loctravels.com/favicon.ico loc/frontend/app/favicon.ico
#   verify-deploy.sh https://pro.impactorsacademy.com/icon.png
#
# Exit 0 = live and (if a repo file was given) byte-identical. Exit 1 = timed out
# or mismatched. Always verify an ASSET, never the HTML — Cloudflare bot-challenges
# pages for non-browser clients but serves static files normally.
set -uo pipefail

URL="${1:?usage: verify-deploy.sh <url> [repo-file] [max-minutes]}"
REPO_FILE="${2:-}"
MAX_MIN="${3:-20}"
CURL=/usr/bin/curl                       # PATH can lack curl in some shells
TMP=$(mktemp); trap 'rm -f "$TMP"' EXIT

sha_of_url() { $CURL -s --max-time 25 -o "$TMP" "$URL" 2>/dev/null && shasum -a256 "$TMP" | cut -d' ' -f1; }
code_of_url() { $CURL -s -o /dev/null -w '%{http_code}' --max-time 20 "$URL" 2>/dev/null || echo ERR; }

want=""
if [ -n "$REPO_FILE" ]; then
  [ -f "$REPO_FILE" ] || { echo "repo file not found: $REPO_FILE" >&2; exit 1; }
  want=$(shasum -a256 "$REPO_FILE" | cut -d' ' -f1)
  echo "target  $URL"
  echo "expect  ${want:0:16}  ($REPO_FILE)"
else
  echo "target  $URL   (availability only — no repo file given)"
fi

start_code=$(code_of_url); start_sha=$(sha_of_url)
echo "start   HTTP $start_code  sha ${start_sha:0:16}"
[ -n "$want" ] && [ "$start_sha" = "$want" ] && { echo "ALREADY LIVE and byte-identical."; exit 0; }

deadline=$(( $(date +%s) + MAX_MIN*60 )); saw503=0; prev="$start_code/$start_sha"
while [ "$(date +%s)" -lt "$deadline" ]; do
  sleep 30
  c=$(code_of_url); s=$(sha_of_url); now="$c/$s"
  [ "$c" = "503" ] && { [ "$saw503" -eq 0 ] && echo "  503 — redeploy in progress (this is the good sign)"; saw503=1; }
  [ "$now" != "$prev" ] && [ "$c" != "503" ] && echo "  HTTP $c  sha ${s:0:16}"
  prev="$now"

  if [ "$c" = "200" ]; then
    if [ -n "$want" ]; then
      [ "$s" = "$want" ] && { echo "LIVE — byte-identical to $REPO_FILE"; exit 0; }
      # 200 but different bytes: either still the old build, or the wrong artifact.
      [ "$s" != "$start_sha" ] && { echo "LIVE but DIFFERS from repo (served ${s:0:16}, expected ${want:0:16})"; exit 1; }
    elif [ "$c" != "$start_code" ] || [ "$s" != "$start_sha" ]; then
      echo "LIVE — HTTP 200, content changed"; exit 0
    fi
  fi
done

echo "TIMED OUT after ${MAX_MIN}m — last HTTP $prev"
[ "$saw503" -eq 0 ] && echo "  Never saw a 503, so no redeploy appears to have started." \
                    && echo "  Check the service's webhook in Coolify before assuming the build failed."
exit 1
