import pandas as pd
import logging

# =====================================================
# LOGGING CONFIGURATION
# =====================================================

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("ETL PIPELINE STARTED")


# -----------------------------
# EXTRACT DEVICE REGISTRY
# -----------------------------

logging.info("Loading Device Registry Data")

device_df = pd.read_json(
    "data/mongo_source/device_registry.json"
)

# Convert dates into datetime

device_df["created_at"] = pd.to_datetime(
    device_df["created_at"],
    errors="coerce"
)

device_df["updated_at"] = pd.to_datetime(
    device_df["updated_at"],
    errors="coerce"
)

# Convert serial number into integer

device_df["serial_number"] = pd.to_numeric(
    device_df["serial_number"],
    errors="coerce"
).astype("Int64")

# Convert is_active into string for validation

device_df["is_active"] = (
    device_df["is_active"]
    .astype("string")
)

# Convert language into string for validation

device_df["language"] = (
    device_df["language"]
    .astype("string")
)

device_list = device_df.to_dict(orient="records")

print("\nDEVICE REGISTRY")
print("Shape :", device_df.shape)
print(device_df.head())

logging.info("Device Registry Loaded Successfully")


# -----------------------------
# EXTRACT REGISTRY AUDIT
# -----------------------------

logging.info("Loading Registry Audit Data")

audit_df = pd.read_json(
    "data/audit_source/registry_audit.json"
)

# Convert dates into datetime

audit_df["created_at"] = pd.to_datetime(
    audit_df["created_at"],
    errors="coerce"
)

# Convert amount into numeric

audit_df["amount"] = pd.to_numeric(
    audit_df["amount"],
    errors="coerce"
)

audit_list = audit_df.to_dict(orient="records")

print("\nREGISTRY AUDIT")
print("Shape :", audit_df.shape)
print(audit_df.head())

logging.info("Registry Audit Loaded Successfully")


# -----------------------------
# VALIDATION
# -----------------------------

print("\n==============================")
print("DEVICE REGISTRY VALIDATION")
print("==============================")

print("\nMissing Values:")
print(device_df.isnull().sum())

print("\nDuplicate Machine Identifier:")
print(
    device_df.duplicated(
        subset=["machine_identifier"]
    ).sum()
)

print("\nDatatypes:")
print(device_df.dtypes)

logging.info("Device Registry Validation Completed")


print("\n==============================")
print("REGISTRY AUDIT VALIDATION")
print("==============================")

print("\nMissing Values:")
print(audit_df.isnull().sum())

print("\nDuplicate Audit IDs:")
print(
    audit_df.duplicated(
        subset=["_id"]
    ).sum()
)

print("\nDatatypes:")
print(audit_df.dtypes)

logging.info("Registry Audit Validation Completed")


# -----------------------------
# CLEANING
# -----------------------------

logging.info("Cleaning Started")

# Remove duplicate records

device_df = device_df.drop_duplicates(
    subset=["machine_identifier"]
)

audit_df = audit_df.drop_duplicates(
    subset=["_id"]
)

# Fill missing amount

audit_df["amount"] = audit_df["amount"].fillna(0)

# Fill missing model

device_df["model"] = device_df["model"].fillna(
    "UNKNOWN_MODEL"
)

# Fill missing serial number

device_df["serial_number"] = (
    device_df["serial_number"]
    .fillna(0)
)

logging.info("Cleaning Completed")


# -----------------------------
# SAVE CLEANED FILES
# -----------------------------

device_df.to_csv(
    "data/processed/device_registry_clean.csv",
    index=False
)

audit_df.to_csv(
    "data/processed/registry_audit_clean.csv",
    index=False
)

print("\nCleaned files saved successfully")

logging.info("Cleaned Files Saved Successfully")


# -----------------------------
# MASTER TABLE CREATION
# -----------------------------

logging.info("Master Table Creation Started")

master_df = audit_df.merge(
    device_df,
    on="machine_identifier",
    how="left",
    suffixes=("_audit", "_device")
)

# Remove redundant nested device column

master_df = master_df.drop(
    columns=["device"]
)

print("\nMASTER TABLE")
print("Shape :", master_df.shape)
print(master_df.head())

logging.info("Master Table Created Successfully")


# -----------------------------
# SAVE MASTER TABLE
# -----------------------------

master_df.to_csv(
    "data/processed/master_device_audit.csv",
    index=False
)

master_df.to_json(
    "data/processed/master_device_audit.json",
    orient="records",
    indent=4,
    date_format="iso"
)

print("\nMaster table saved successfully")

logging.info("Master Table Saved Successfully")

logging.info("ETL PIPELINE COMPLETED")