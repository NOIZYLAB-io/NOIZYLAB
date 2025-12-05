# 📊 Power BI Export Guide

## Quick Export

### From CLI Menu
```bash
python email_intelligence_v2.py
# Choose option 5 → 2 (Power BI export)
```

### Standalone Script
```bash
python powerbi_export.py
# Or with custom paths:
python powerbi_export.py email_intelligence.db powerbi_export.csv
```

### Automatic Export
After processing a CSV, you'll be prompted to export to Power BI format automatically.

## Power BI Format

The export includes:
- ✅ All email data
- ✅ Spam scores (as percentages)
- ✅ Validity scores (as percentages)
- ✅ Flattened JSON fields
- ✅ Date formatting for Power BI
- ✅ Optimized column names

## Columns Exported

1. `id` - Unique identifier
2. `email` - Email address
3. `category` - Category (personal/business/spam)
4. `spam_score_percent` - Spam score (0-100%)
5. `validity_score_percent` - Validity score (0-100%)
6. `is_disposable` - Boolean (0/1)
7. `language_detected` - ISO language code
8. `company_name` - Detected company
9. `confidence_score` - AI confidence (0-100)
10. `processed_at` - Processing timestamp
11. `updated_at` - Last update timestamp
12. `enrichment` - AI enrichment data
13. `spam_indicators` - Spam indicators list
14. `ai_category` - AI-detected category

## Importing to Power BI

1. Open Power BI Desktop
2. Get Data → Text/CSV
3. Select `powerbi_export.csv`
4. Data will be automatically formatted
5. Create visualizations!

## Tips

- **Refresh**: Re-export after processing new emails
- **Filtering**: Use spam_score_percent > 70 for high-risk emails
- **Grouping**: Group by category for insights
- **Trends**: Use processed_at for time-based analysis

## Example Power BI Queries

```dax
// High-risk spam emails
High Risk Spam = 
FILTER(
    'email_list',
    'email_list'[spam_score_percent] > 70
)

// Category breakdown
Category Count = 
COUNTROWS(
    GROUPBY(
        'email_list',
        'email_list'[category]
    )
)
```

---

**Ready for Power BI analysis!** 📊✨

