# MHC_LLM_Preference_Data

This repository contains the Human Expert vs. LLM Preference Data from the My Heart Counts study. It includes raw and processed datasets, a comprehensive list of messages, a mapping dictionary for customization, and a script to process the data.

## Directory Structure

- **data/**
  - **raw/**: Contains the raw dataset (`pref_data_raw.csv`)
  - **processed/**: Contains the processed dataset (`pref_data_processed.csv`)
- **scripts/**
  - `process_data.py`: Script to process the data
  - `mapping.json`: Mapping dictionary for customization
- **docs/**
  - `messages.md`: Full list of messages
- `README.md`: This file

---

## Usage Instructions

### Step 1: Customize `mapping.json`

The `mapping.json` file defines descriptions and mappings for each column in the dataset. You can edit it to:

- Adjust column mappings (e.g., update `Gender` or `Stage of Change` labels).
- Modify message preferences or add new mappings.

### Step 2: Run `process_data.py`

To process the raw dataset and apply your mappings:

1. Navigate to the `scripts` folder:

   ```bash
   cd scripts

   ```

2. Run the script:

   ```bash
   python3 process_data.py

   ```

3. The processed file will be saved in:
   ```bash
   data/processed/pref_data_processed.csv
   ```

Notes on the Survey

- Participants only answered stage-specific questions corresponding to their current stage of change. For example, individuals in the "Action" stage only answered questions related to that stage. Columns unrelated to their stage are intentionally left blank.
- The LLM messages were generated using a fine-tuned version of LLaMA3-70B.

## Messages

For the full list of messages, refer to the [data/messages.md](./data/messages.md) file.
