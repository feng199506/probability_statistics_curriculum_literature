#!/usr/bin/env bash
# Resume every PSCL download step (idempotent: verified items are skipped, files never overwritten).
#   bash scripts/resume_all_en.sh            # pending items only
#   bash scripts/resume_all_en.sh --retry    # also retry items that failed before
# Run from anywhere; one instance at a time (flock).
set -u
LIB="$(cd "$(dirname "$0")/.." && pwd)"
cd "$LIB"
exec 9>/root/.cache/pscl_lit/resume.lock
flock -n 9 || { echo "another resume_all_en.sh is running"; exit 1; }
R=""; [ "${1:-}" = "--retry" ] && R="--retry-failed"
for g in 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 20; do
  python3 -I scripts/papers_en.py download "$g" $R
done
for s in curricula courses books practice cases software; do
  python3 -I scripts/materials_en.py fetch "$s" $R
done
python3 -I scripts/build_catalog_en.py
python3 -I scripts/search_log_en.py
