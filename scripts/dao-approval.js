const core = require('@actions/core');
const github = require('@actions/github');

// DAO Governance Rules
const MIN_APPROVALS = 2;
const MIN_COMMITS = 5;
const QUORUM_PERCENT = 51;

async function run() {
  try {
    const token = core.getInput('github-token');
    const octokit = github.getOctokit(token);
    
    // Get PR details
    const { pull_request: pr } = github.context.payload;
    
    // 1. Check contributor status
    const commits = await octokit.rest.pulls.listCommits({
      owner: github.context.repo.owner,
      repo: github.context.repo.repo,
      pull_number: pr.number
    });
    
    const contributors = new Set(commits.data.map(c => c.author.login));
    
    // 2. Verify DAO votes
    const daoResponse = await octokit.rest.issues.listComments({
      owner: 'eqdi-dao',
      repo: 'governance',
      issue_number: pr.number
    });
    
    const approvals = daoResponse.data.filter(c => 
      c.body.includes('/approve') &&
      isVerifiedMember(c.user.login)
    ).length;

    // 3. Check quorum
    const totalMembers = await getDAOMembers();
    const quorum = (approvals / totalMembers) * 100;
    
    if (approvals >= MIN_APPROVALS && quorum >= QUORUM_PERCENT) {
      core.info(`DAO approval granted with ${approvals} votes (${quorum.toFixed(1)}% quorum)`);
    } else {
      core.setFailed(`Insufficient DAO approval: ${approvals}/${MIN_APPROVALS} votes, ${quorum.toFixed(1)}%/${QUORUM_PERCENT}% quorum`);
    }

  } catch (error) {
    core.setFailed(error.message);
  }
}

async function isVerifiedMember(username) {
  // Check commit history for verification
  const commits = await octokit.rest.repos.listCommits({
    owner: github.context.repo.owner,
    repo: github.context.repo.repo,
    author: username
  });
  
  return commits.data.length >= MIN_COMMITS;
}

async function getDAOMembers() {
  // Get DAO NFT holders from blockchain (simulated)
  return 42; // Replace with actual on-chain call
}

run();
