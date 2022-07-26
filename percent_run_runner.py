# Databricks notebook source
dbutils.widgets.text("input_parameter_path", "na")

# COMMAND ----------

input_parameter_path = dbutils.widgets.get("input_parameter_path")
input_note = dbutils.notebook.run(input_parameter_path,0)

# COMMAND ----------

print(input_note)
