#!/usr/bin/env bash
# Verify that every relative Markdown link and image target exists.
set -uo pipefail

broken=0

while IFS= read -r file; do
  dir=$(dirname "$file")

  # Pull targets out of [text](target) and ![alt](target).
  # Drop absolute URLs, mailto:, and pure #anchors. A file with none is fine.
  targets=$(grep -oE '\]\([^)]+\)' "$file" 2>/dev/null \
              | sed -e 's/^](//' -e 's/)$//' -e 's/#.*$//' \
              | grep -vE '^(https?|mailto):' \
              | grep -v '^$' || true)

  [ -z "$targets" ] && continue

  while IFS= read -r target; do
    if [ ! -e "$dir/$target" ]; then
      echo "broken link: $file -> $target"
      broken=$((broken + 1))
    fi
  done <<< "$targets"
done < <(find . -name '*.md' -not -path './.git/*' | sort)

if [ "$broken" -gt 0 ]; then
  echo "$broken broken link(s)."
  exit 1
fi
echo "All relative links resolve."
