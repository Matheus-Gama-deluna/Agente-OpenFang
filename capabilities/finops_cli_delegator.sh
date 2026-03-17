#!/bin/bash
# FinOps CLI Delegator for Maestro Operator Agent
# This script wraps the local 'gemini-cli' to parse large logs without consuming OpenFang's token budget
# Usage: ./finops_cli_delegator.sh "prompt string" "path/to/log.txt"

PROMPT=$1
LOG_FILE_PATH=$2

# Security check: Ensure the log file is within the allowed safe directory Mount
SAFE_DIR="/app/safelogs"

if [[ "$LOG_FILE_PATH" != "$SAFE_DIR/"* ]]; then
    echo "ERROR: SECURITY EXCEPTION. Attemped to access files outside the secure $SAFE_DIR directory."
    exit 1
fi

if [ ! -f "$LOG_FILE_PATH" ]; then
    echo "ERROR: The file $LOG_FILE_PATH does not exist."
    exit 1
fi

# We assume gemini-cli is installed and authenticated on the host (or injected via image)
echo "[FinOps Delegator] Sending job to Gemini CLI for processing..."
# Using the PRO-tier free quota via CLI instead of OpenFang's Pay-as-you-go context windows
gemini-cli prompt "$PROMPT" --file "$LOG_FILE_PATH"

# Output is routed back to OpenFang agent
