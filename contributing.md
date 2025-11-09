Contributing to AuditFlow Agent Core

We are thrilled you're interested in contributing! This project is powered by the community, and every contribution helps make automated auditing safer and more efficient.

🐛 Found a Bug?

Before submitting a bug report, please check the existing issues to see if the problem has already been reported.

Open a new GitHub Issue.

Provide a clear, descriptive title.

Include steps to reproduce the issue (the commands you ran, configuration settings).

Specify your operating system and Python version.

🌟 Have a Feature Idea?

We love new ideas, especially for new audit modules or improvements to the core execution engine!

Open a new GitHub Issue.

Use the title to summarize the feature (e.g., "Feature Request: Add Kubernetes Audit Module").

Describe the problem the feature solves and the value it adds to the Agent Core.

💻 Code Contributions

1. Setup

# Fork the repository first
git clone git@github.com:[YOUR_USERNAME]/auditflow-agent-core.git
cd auditflow-agent-core
pip install -e .[dev] # Install development dependencies


2. Testing

All new code should have corresponding tests. We use pytest.

pytest


3. Submitting Your Pull Request (PR)

Create a new branch for your work (git checkout -b feature/my-great-module).

Commit your changes, using clear, descriptive messages.

Push your branch and open a Pull Request against the main branch.

In the PR description, reference any related issues (e.g., "Fixes #123").

Thank you for making AuditFlow Core better!
