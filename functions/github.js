require('dotenv').config();
const GitHubPublisher = require('github-publish');
const moment = require('moment');

const { GITHUB_TOKEN, GITHUB_USER, GITHUB_REPO } = process.env

const gitpush = async(data) => {
    return new Promise((resolve) => {
      const publisher = new GitHubPublisher(GITHUB_TOKEN, GITHUB_USER, GITHUB_REPO, 'main');
      const path = "data/news/"
      
      const { anglais, francais, wolof } = data.data
      const { created_at: date } = data
      let filename = `${path}word-${moment(date).format("YYYY-MM-DD-HH-mm")}.csv`
      let filecontent = `${wolof},${francais},${anglais}`
      publisher.publish(filename, filecontent, { message: 'Form add new word' }).then(function (result) {
      // If "result" is truthy then the post was successfully published
      resolve("Enregister")
      });

  })
}

module.exports = gitpush