# Data Quality Audit & Cleaning Report

## Executive Summary
This report documents the structural evaluation and cleaning pipeline executed on the e-commerce sales dataset.

## 1. Dataset Overview
- **Total Records Analyzed**: 2,000
- **Primary Attributes**: Order_ID, Order_Date, Customer_ID, Product, Category, Region, Quantity, Revenue, Profit.

## 2. Issues Identified
1. **Duplicates**: 23 identical rows found.
2. **Inconsistent Casing**: Category and Region fields contained mixed casing (`electronics`, `ELECTRONICS`, `Electronics`).
3. **Currency Symbols**: `Revenue` column contained non-numeric currency characters (`₹`).
4. **Invalid Entries**: Negative order quantities (-3, -5) and unparseable dates (`31-02-2026`).

## 3. Data Cleaning Pipeline Actions
- Deduplicated all identical rows.
- Converted all categorical fields (`Category`, `Region`) to standard Title Case.
- Extracted raw numerical values from `Revenue`.
- Corrected/flagged negative quantities and invalid calendar dates.

## 4. Next Steps
- Export cleaned CSV into dashboarding tools (Tableau / Power BI) for executive reporting.
