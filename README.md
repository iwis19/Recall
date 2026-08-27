# Recall
Simple RAG tool built in Python &amp; Flask

still need to work on:
- learning js + flask
- reinforce python oop knowledge
- build hybrid search, evals, etc rather than just a vectordb wrapper
- optimize speed

issue:
- In huge enterprise repos, your own commits get buried under everyone else's changes
- Search your personal Git history using natural language, e.g. “when did I change the caching logic?”
- RAG over your authored commits + actual code diffs, not just commit messages
- Flask + Python handles Git parsing, embeddings, hybrid search, reranking, etc.
- Build a simple Flask web app first to learn web development and get the RAG pipeline working
- Later add a lightweight VS Code extension that talks to the same Flask API
- Search and jump back to your past changes without leaving VS Code
- Semantic search specifically over your historical code changes, rather than normal Git/commit search

focus on:
- representing diffs so semantic search works well.
- searching individual hunks but returning coherent commits.
- handling renames, merges, reverts, lockfiles, generated files, and huge commits.
- determining which commits belong to the developer across multiple emails/usernames.
- incrementally indexing new commits without duplicating old records.
- evaluating whether semantic search beats ordinary git log, keyword search, and commit-message search.
- opening the correct historical file/diff location from VS Code.

relevant info:
- commit message
- file path
- diff-hunk header
- approximately 10–20 unchanged context lines
- clearly separated additions and deletions
- containing Python function/class when detectable
- other changed filenames
- hybrid search and reranking
- exact diff display