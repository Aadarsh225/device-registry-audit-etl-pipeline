import pandas as pd
import great_expectations as gx

print("=" * 60)
print("GREAT EXPECTATIONS DATA QUALITY CHECK")
print("=" * 60)

# =====================================================
# LOAD FILES
# =====================================================

device_df = pd.read_csv(
    "data/processed/device_registry_clean.csv"
)

audit_df = pd.read_csv(
    "data/processed/registry_audit_clean.csv"
)

master_df = pd.read_json(
    "data/processed/master_device_audit.json"
)

print("\nDevice Registry Shape :", device_df.shape)
print("Registry Audit Shape :", audit_df.shape)
print("Master Table Shape :", master_df.shape)


# =====================================================
# CREATE CONTEXT
# =====================================================

context = gx.get_context()


# =====================================================
# DEVICE REGISTRY VALIDATION
# =====================================================

device_source = context.data_sources.add_pandas(
    name="device_source"
)

device_asset = device_source.add_dataframe_asset(
    name="device_asset"
)

device_batch_definition = (
    device_asset.add_batch_definition_whole_dataframe(
        "device_batch"
    )
)

device_batch_request = (
    device_batch_definition.build_batch_request(
        {"dataframe": device_df}
    )
)

device_suite = context.suites.add_or_update(
    gx.ExpectationSuite(
        name="device_validation_suite"
    )
)

device_validator = context.get_validator(
    batch_request=device_batch_request,
    expectation_suite=device_suite
)

print("\nRUNNING DEVICE REGISTRY EXPECTATIONS...\n")

device_validator.expect_column_values_to_not_be_null(
    "machine_identifier"
)

device_validator.expect_column_values_to_be_unique(
    "machine_identifier"
)

device_validator.expect_column_values_to_not_be_null(
    "serial_number"
)

device_validator.expect_column_values_to_be_in_set(
    "type",
    ["static", "dynamic", "unknown"]
)

device_validator.expect_column_values_to_not_be_null(
    "created_at"
)

device_validator.expect_column_values_to_not_be_null(
    "updated_at"
)

device_results = device_validator.validate()


# =====================================================
# REGISTRY AUDIT VALIDATION
# =====================================================

audit_source = context.data_sources.add_pandas(
    name="audit_source"
)

audit_asset = audit_source.add_dataframe_asset(
    name="audit_asset"
)

audit_batch_definition = (
    audit_asset.add_batch_definition_whole_dataframe(
        "audit_batch"
    )
)

audit_batch_request = (
    audit_batch_definition.build_batch_request(
        {"dataframe": audit_df}
    )
)

audit_suite = context.suites.add_or_update(
    gx.ExpectationSuite(
        name="audit_validation_suite"
    )
)

audit_validator = context.get_validator(
    batch_request=audit_batch_request,
    expectation_suite=audit_suite
)

print("\nRUNNING REGISTRY AUDIT EXPECTATIONS...\n")

audit_validator.expect_column_values_to_be_unique(
    "_id"
)

audit_validator.expect_column_values_to_not_be_null(
    "machine_identifier"
)

audit_validator.expect_column_values_to_be_between(
    "amount",
    min_value=0
)

audit_validator.expect_column_values_to_be_in_set(
    "status",
    ["SUCCESS", "FAILED", "PENDING", "FIRED"]
)

audit_validator.expect_column_values_to_not_be_null(
    "created_at"
)

audit_results = audit_validator.validate()


# =====================================================
# MASTER TABLE VALIDATION
# =====================================================

master_source = context.data_sources.add_pandas(
    name="master_source"
)

master_asset = master_source.add_dataframe_asset(
    name="master_asset"
)

master_batch_definition = (
    master_asset.add_batch_definition_whole_dataframe(
        "master_batch"
    )
)

master_batch_request = (
    master_batch_definition.build_batch_request(
        {"dataframe": master_df}
    )
)

master_suite = context.suites.add_or_update(
    gx.ExpectationSuite(
        name="master_validation_suite"
    )
)

master_validator = context.get_validator(
    batch_request=master_batch_request,
    expectation_suite=master_suite
)

print("\nRUNNING MASTER TABLE EXPECTATIONS...\n")

master_validator.expect_column_values_to_not_be_null(
    "machine_identifier"
)

master_validator.expect_column_values_to_be_unique(
    "_id_audit"
)

master_validator.expect_column_values_to_be_between(
    "amount",
    min_value=0
)

master_validator.expect_column_values_to_be_in_set(
    "status",
    ["SUCCESS", "FAILED", "PENDING", "FIRED"]
)

master_validator.expect_column_values_to_not_be_null(
    "serial_number"
)

master_validator.expect_column_values_to_not_be_null(
    "created_at_audit"
)

master_validator.expect_column_values_to_not_be_null(
    "created_at_device"
)

master_results = master_validator.validate()


# =====================================================
# PRINT RESULTS
# =====================================================

print("\nDEVICE REGISTRY VALIDATION :", device_results["success"])

for result in device_results["results"]:
    print(
        result["expectation_config"]["type"],
        "->",
        result["success"]
    )


print("\nREGISTRY AUDIT VALIDATION :", audit_results["success"])

for result in audit_results["results"]:
    print(
        result["expectation_config"]["type"],
        "->",
        result["success"]
    )


print("\nMASTER TABLE VALIDATION :", master_results["success"])

for result in master_results["results"]:
    print(
        result["expectation_config"]["type"],
        "->",
        result["success"]
    )


# =====================================================
# NULL VALUE SUMMARY
# =====================================================

print("\nDEVICE REGISTRY NULL VALUES")
print(device_df.isnull().sum())

print("\nREGISTRY AUDIT NULL VALUES")
print(audit_df.isnull().sum())

print("\nMASTER TABLE NULL VALUES")
print(master_df.isnull().sum())


# =====================================================
# SAVE EXPECTATION SUITES
# =====================================================

context.suites.add_or_update(
    device_validator.expectation_suite
)

context.suites.add_or_update(
    audit_validator.expectation_suite
)

context.suites.add_or_update(
    master_validator.expectation_suite
)

print("\nGreat Expectations Validation Completed")
print("=" * 60)