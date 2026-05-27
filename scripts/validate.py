import pandas as pd

print("=" * 60)
print("DATA VALIDATION")
print("=" * 60)

# =====================================================
# LOAD CLEANED FILES
# =====================================================

device_df = pd.read_csv(
    "data/processed/device_registry_clean.csv"
)

audit_df = pd.read_csv(
    "data/processed/registry_audit_clean.csv"
)

print("\nDevice Registry Shape :", device_df.shape)

print("Registry Audit Shape :", audit_df.shape)


# =====================================================
# DEVICE REGISTRY VALIDATION
# =====================================================

print("\n==============================")
print("DEVICE REGISTRY VALIDATION")
print("==============================")


# Missing values

device_nulls = (
    device_df.isnull()
    .sum()
)

print("\nMISSING VALUES")
print(device_nulls)


# Duplicate machine identifiers

device_duplicates = (
    device_df.duplicated(
        subset=["machine_identifier"]
    ).sum()
)

print("\nDUPLICATE MACHINE IDENTIFIERS")
print(device_duplicates)


# Datatypes

print("\nDATATYPES")
print(device_df.dtypes)


# Invalid type values

invalid_type = (
    ~device_df["type"]
    .isin(["static", "dynamic", "unknown"])
).sum()

print("\nINVALID DEVICE TYPES")
print(invalid_type)


# Invalid serial number

invalid_serial = (
    device_df["serial_number"]
    .isnull()
    .sum()
)

print("\nINVALID SERIAL NUMBERS")
print(invalid_serial)


# =====================================================
# REGISTRY AUDIT VALIDATION
# =====================================================

print("\n==============================")
print("REGISTRY AUDIT VALIDATION")
print("==============================")


# Missing values

audit_nulls = (
    audit_df.isnull()
    .sum()
)

print("\nMISSING VALUES")
print(audit_nulls)


# Duplicate audit ids

audit_duplicates = (
    audit_df.duplicated(
        subset=["_id"]
    ).sum()
)

print("\nDUPLICATE AUDIT IDS")
print(audit_duplicates)


# Datatypes

print("\nDATATYPES")
print(audit_df.dtypes)


# Invalid status values

invalid_status = (
    ~audit_df["status"]
    .isin([
        "SUCCESS",
        "FAILED",
        "PENDING",
        "FIRED"
    ])
).sum()

print("\nINVALID STATUS VALUES")
print(invalid_status)


# Negative amount check

negative_amount = (
    audit_df["amount"] < 0
).sum()

print("\nNEGATIVE AMOUNTS")
print(negative_amount)


# =====================================================
# CREATE VALIDATION REPORT
# =====================================================

validation_report = pd.DataFrame({

    "Validation": [

        "Device Null Values",
        "Device Duplicate Machine IDs",
        "Invalid Device Types",
        "Invalid Serial Numbers",

        "Audit Null Values",
        "Audit Duplicate IDs",
        "Invalid Status",
        "Negative Amount"

    ],

    "Count": [

        device_nulls.sum(),
        device_duplicates,
        invalid_type,
        invalid_serial,

        audit_nulls.sum(),
        audit_duplicates,
        invalid_status,
        negative_amount
    ]
})


# =====================================================
# SAVE REPORT
# =====================================================

validation_report.to_csv(
    "reports/validation_report.csv",
    index=False
)

print("\nValidation Report Saved Successfully")

print("=" * 60)