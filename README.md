# CodeGuard Platform

A backend code analysis and CI enforcement platform that detects correctness,
performance, and security regressions in pull requests.

## Features
- Deterministic analysis engines
- Policy-based enforcement
- CI and Jira-ready escalation model

## Run locally
pip install -r requirements.txt
uvicorn app.main:app --reload
