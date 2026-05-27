import os

print("=" * 60)
print("DEVICE REGISTRY & AUDIT ETL PIPELINE")
print("=" * 60)


# =====================================================
# RUN ETL
# =====================================================

print("\nRUNNING ETL PIPELINE...\n")

os.system(
    "python scripts/etl.py"
)

print("\nETL COMPLETED")


# =====================================================
# RUN VALIDATION
# =====================================================

print("\nRUNNING VALIDATION...\n")

os.system(
    "python scripts/validate.py"
)

print("\nVALIDATION COMPLETED")


# =====================================================
# RUN MASTER TABLE
# =====================================================

print("\nRUNNING MASTER TABLE CREATION...\n")

os.system(
    "python scripts/master_table.py"
)

print("\nMASTER TABLE CREATED")


# =====================================================
# RUN GREAT EXPECTATIONS
# =====================================================

print("\nRUNNING GREAT EXPECTATIONS...\n")

os.system(
    "python scripts/great_expectation_check.py"
)

print("\nGREAT EXPECTATIONS COMPLETED")


# =====================================================
# RUN ANALYTICS
# =====================================================

print("\nRUNNING ANALYTICS...\n")

os.system(
    "python scripts/analytics.py"
)

print("\nANALYTICS COMPLETED")


# =====================================================
# PIPELINE FINISHED
# =====================================================

print("\n" + "=" * 60)
print("FULL PIPELINE EXECUTED SUCCESSFULLY")
print("=" * 60)