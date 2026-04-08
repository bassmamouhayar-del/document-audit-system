def apply_rules(doc):
    rules = []

    # تحقق منطقي
    if not doc["weight"]:
        rules.append("❌ [CRITICAL] الوزن غير موجود")

    if not doc["packages"]:
        rules.append("❌ [CRITICAL] عدد الطرود غير موجود")

    # مثال تحقق
    if doc["total"] and float(doc["total"][0]) < 100:
        rules.append("⚠️ [WARNING] قيمة منخفضة مشبوهة")

    return rules
