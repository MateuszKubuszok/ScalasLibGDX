#!/bin/bash
cd /Users/dev/Workspaces/kubuszok/sge
S=$1
for lib in textratypist colorful-gdx gdx-gltf vis-ui gdx-ai gdx-controllers anim8-gdx libgdx; do
  c=$(git ls-tree HEAD original-src/$lib | awk '{print $3}')
  G=.git/modules/original-src/$lib
  git --git-dir=$G ls-tree -r --name-only $c | grep '\.java$' > $S/tree_$lib.txt
  awk -F'\t' -v L=$lib '$7==L && $3!="skip"{print $1}' .rescale/data/migration.tsv | sort -u > $S/src_$lib.txt
  tot=0; found=0; miss=0
  while read p; do
    m=$(grep -m1 "/$p\$" $S/tree_$lib.txt)
    if [ -n "$m" ]; then n=$(git --git-dir=$G show $c:$m | wc -l); tot=$((tot+n)); found=$((found+1)); else miss=$((miss+1)); fi
  done < $S/src_$lib.txt
  echo "$lib rows=$(wc -l <$S/src_$lib.txt) matched=$found unmatched=$miss upstreamLOC=$tot"
done
