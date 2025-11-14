-- ===================================================
-- 🩺 Slowly Changing Dimension (Type 2)
-- Table: SILVER_LAYER.dim_patient
-- ===================================================

-- STEP 1: Close existing records that changed
MERGE `even-blueprint-441418-p2.SILVER_LAYER.dim_patient` AS dim
USING (
  SELECT
    st.patient_id,
    st.first_name,
    st.last_name,
    st.gender
  FROM `even-blueprint-441418-p2.SILVER_LAYER.stg_patient` AS st
  JOIN `even-blueprint-441418-p2.SILVER_LAYER.dim_patient` AS dim0
    ON st.patient_id = dim0.patient_id
   AND dim0.is_current_flag = TRUE
  WHERE
    st.first_name IS DISTINCT FROM dim0.first_name
    OR st.last_name IS DISTINCT FROM dim0.last_name
    OR st.gender IS DISTINCT FROM dim0.gender
) AS changes
ON dim.patient_id = changes.patient_id
AND dim.is_current_flag = TRUE
WHEN MATCHED THEN
  UPDATE SET
    dim.end_date = CURRENT_DATE(),
    dim.is_current_flag = FALSE;

-- STEP 2: Insert new or changed records
INSERT INTO `even-blueprint-441418-p2.SILVER_LAYER.dim_patient`
  (
    patient_id,
    first_name,
    last_name,
    gender,
    start_date,
    end_date,
    is_current_flag
  )
SELECT
  st.patient_id,
  st.first_name,
  st.last_name,
  st.gender,
  CURRENT_DATE() AS start_date,
  NULL AS end_date,
  TRUE AS is_current_flag
FROM `even-blueprint-441418-p2.SILVER_LAYER.stg_patient` AS st
LEFT JOIN `even-blueprint-441418-p2.SILVER_LAYER.dim_patient` AS dim1
  ON st.patient_id = dim1.patient_id
 AND dim1.is_current_flag = TRUE
WHERE
  dim1.patient_id IS NULL
  OR st.first_name IS DISTINCT FROM dim1.first_name
  OR st.last_name IS DISTINCT FROM dim1.last_name
  OR st.gender IS DISTINCT FROM dim1.gender;
