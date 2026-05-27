import pandas as pd

print("=" * 60)
print("DEVICE REGISTRY & AUDIT ANALYTICS")
print("=" * 60)

# =====================================================
# LOAD MASTER TABLE
# =====================================================

master_df = pd.read_csv(
    "data/processed/master_device_audit.csv"
)

print("\nMaster Table Shape :", master_df.shape)


# =====================================================
# BASIC ANALYTICS
# =====================================================

total_transactions = master_df.shape[0]

total_amount = master_df["amount"].sum()

average_amount = master_df["amount"].mean()

max_amount = master_df["amount"].max()

min_amount = master_df["amount"].min()


# =====================================================
# STATUS ANALYTICS
# =====================================================

success_transactions = (
    master_df[
        master_df["status"] == "SUCCESS"
    ].shape[0]
)

failed_transactions = (
    master_df[
        master_df["status"] == "FAILED"
    ].shape[0]
)

pending_transactions = (
    master_df[
        master_df["status"] == "PENDING"
    ].shape[0]
)

fired_transactions = (
    master_df[
        master_df["status"] == "FIRED"
    ].shape[0]
)


# =====================================================
# PAYMENT SCHEME ANALYTICS
# =====================================================

scheme_usage = (
    master_df["scheme"]
    .value_counts()
)

scheme_amount = (
    master_df.groupby("scheme")["amount"]
    .sum()
)


# =====================================================
# DEVICE TYPE ANALYTICS
# =====================================================

device_type_usage = (
    master_df["type"]
    .value_counts()
)

active_devices = (
    master_df[
        master_df["is_active"] == True
    ].shape[0]
)

inactive_devices = (
    master_df[
        master_df["is_active"] == False
    ].shape[0]
)


# =====================================================
# MODEL ANALYTICS
# =====================================================

top_models = (
    master_df["model"]
    .value_counts()
)


# =====================================================
# NULL VALUE ANALYTICS
# =====================================================

null_summary = (
    master_df.isnull()
    .sum()
)

total_nulls = null_summary.sum()


# =====================================================
# DUPLICATE ANALYTICS
# =====================================================

duplicate_machine_identifier = (
    master_df.duplicated(
        subset=["machine_identifier"]
    ).sum()
)

duplicate_audit_ids = (
    master_df.duplicated(
        subset=["_id_audit"]
    ).sum()
)


# =====================================================
# DATE ANALYTICS
# =====================================================

master_df["created_at_audit"] = pd.to_datetime(
    master_df["created_at_audit"],
    errors="coerce"
)

earliest_transaction = (
    master_df["created_at_audit"]
    .min()
)

latest_transaction = (
    master_df["created_at_audit"]
    .max()
)


# =====================================================
# PRINT ANALYTICS
# =====================================================

print("\nTOTAL TRANSACTIONS :", total_transactions)

print("\nTOTAL AMOUNT :", total_amount)

print("\nAVERAGE AMOUNT :", average_amount)

print("\nMAX AMOUNT :", max_amount)

print("\nMIN AMOUNT :", min_amount)


print("\nSUCCESS TRANSACTIONS :", success_transactions)

print("\nFAILED TRANSACTIONS :", failed_transactions)

print("\nPENDING TRANSACTIONS :", pending_transactions)

print("\nFIRED TRANSACTIONS :", fired_transactions)


print("\nPAYMENT SCHEME USAGE")
print(scheme_usage)

print("\nPAYMENT SCHEME AMOUNT")
print(scheme_amount)


print("\nDEVICE TYPE USAGE")
print(device_type_usage)

print("\nACTIVE DEVICES :", active_devices)

print("\nINACTIVE DEVICES :", inactive_devices)


print("\nTOP DEVICE MODELS")
print(top_models)


print("\nNULL VALUE SUMMARY")
print(null_summary)

print("\nTOTAL NULL VALUES :", total_nulls)


print("\nDUPLICATE MACHINE IDENTIFIERS :")
print(duplicate_machine_identifier)

print("\nDUPLICATE AUDIT IDS :")
print(duplicate_audit_ids)


print("\nEARLIEST TRANSACTION :")
print(earliest_transaction)

print("\nLATEST TRANSACTION :")
print(latest_transaction)


# =====================================================
# CREATE ANALYTICS REPORT
# =====================================================

analytics_report = pd.DataFrame({
    "Metric": [
        "Total Transactions",
        "Total Amount",
        "Average Amount",
        "Max Amount",
        "Min Amount",
        "Success Transactions",
        "Failed Transactions",
        "Pending Transactions",
        "Fired Transactions",
        "Active Devices",
        "Inactive Devices",
        "Duplicate Machine Identifier",
        "Duplicate Audit IDs",
        "Total Null Values"
    ],

    "Value": [
        total_transactions,
        total_amount,
        average_amount,
        max_amount,
        min_amount,
        success_transactions,
        failed_transactions,
        pending_transactions,
        fired_transactions,
        active_devices,
        inactive_devices,
        duplicate_machine_identifier,
        duplicate_audit_ids,
        total_nulls
    ]
})


# =====================================================
# SAVE REPORT
# =====================================================

analytics_report.to_csv(
    "reports/analytics_report.csv",
    index=False
)

print("\nAnalytics Report Saved Successfully")

print("=" * 60)