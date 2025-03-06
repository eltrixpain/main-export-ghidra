#!/bin/bash

# change the variable based on your vars.
GHIDRA_HEADLESS="./analyzeHeadless"  
PROJECT_PATH="$HOME/Desktop/ghp"     
PROJECT_NAME="ghp"                   
POST_SCRIPT="export_main.py"         
OUTPUT_DIR="/tmp/hamid"     

mkdir -p "$OUTPUT_DIR"

PROGRAMS=("a.out" "first" "second" "third")  # Modify this list

for PROGRAM_NAME in "${PROGRAMS[@]}"; do
    OUTPUT_FILE="$OUTPUT_DIR/${PROGRAM_NAME}_export.txt"

    echo "Running Ghidra headless analysis for function: $PROGRAM_NAME"
    
    $GHIDRA_HEADLESS "$PROJECT_PATH" "$PROJECT_NAME" \
        -import "$PROGRAM_NAME" -overwrite \
        -postScript "$POST_SCRIPT" "$PROGRAM_NAME"

    echo "Export saved to: $OUTPUT_FILE"
done

echo "All functions processed."

