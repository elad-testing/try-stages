mkdir travis_results
LINK_DIR=travis_results/download_link.txt
touch $LINK_DIR
"bla bla" > $LINK_DIR

if [[ -f "$LINK_DIR" ]]; then
  DOWNLOAD_LINK=$(<$LINK_DIR)
  echo ${DOWNLOAD_LINK}
  COMMENT="Download your test results [here](${DOWNLOAD_LINK}) (html file)"
  curl -H "Authorization: token $TOKEN" -X POST -d "{\"body\": \"$COMMENT\"}" "https://api.github.com/repos/$TRAVIS_REPO_SLUG/issues/$TRAVIS_PULL_REQUEST/comments"
else
  echo no results to deploy
fi
