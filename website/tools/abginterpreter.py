def determine_acid_base_balance(
    ph_value,
    pco2,
    bicarbonate,
    sodium,
    chloride,
    measured_serum_osmolality,
    glucose,
    urea,
):
    normal_bicarbonate = 24.0

    if 7.35 <= ph_value <= 7.45:
        acid_base_status = "Normal (Physiological) pH"
    elif ph_value < 7.35:
        acid_base_status = "Acidosis"
    else:
        acid_base_status = "Alkalosis"

    if acid_base_status == "Acidosis" and pco2 < 35:
        cause = "Metabolic Acidosis"
    elif acid_base_status == "Acidosis" and pco2 > 45:
        cause = "Respiratory Acidosis"
    elif acid_base_status == "Alkalosis" and pco2 > 45:
        cause = "Metabolic Alkalosis"
    elif acid_base_status == "Alkalosis" and pco2 > 35:
        cause = "Respiratory Alkalosis"
    else:
        cause = "Uncertain cause"

    if cause == "Metabolic Acidosis":
        anion_gap = sodium - (chloride + bicarbonate)
        if anion_gap > 12:
            gap_type = "High Anion Gap Metabolic Acidosis (HAGMA)"
        else:
            gap_type = "Normal Anion Gap Metabolic Acidosis (NAGMA)"
        # Calculate osmolal gap in HAGMA
        osmolal_gap = measured_serum_osmolality - 2 * (sodium) - (urea + glucose)
    else:
        gap_type = "Not applicable"

    if cause == "Respiratory Acidosis" and acid_base_status == "Acidosis":
        # Calculate expected change in HCO3- for respiratory acidosis
        expected_change_acute = 0.1 * (pco2 - 45)
        expected_change_chronic = 0.4 * (pco2 - 45)

    elif cause == "Respiratory Alkalosis" and acid_base_status == "Alkalosis":
        # Calculate expected change in HCO3- for respiratory alkalosis
        expected_change_acute = -0.2 * (35 - pco2)
        expected_change_chronic = -0.5 * (35 - pco2)

    else:
        expected_change_acute = None
        expected_change_chronic = None

    if cause == "Metabolic Acidosis" and acid_base_status == "Acidosis":
        # Check for respiratory compensation in metabolic acidosis
        expected_pco2 = 1.5 * bicarbonate + 8
        if pco2 > (expected_pco2 + 2):
            respiratory_compensation = "Inadequate compensation"
        elif pco2 < (expected_pco2 - 2):
            respiratory_compensation = (
                "Excessive compensation (concomitant respiratory alkalosis)"
            )
        else:
            respiratory_compensation = "Adequate compensation"
    elif cause == "Metabolic Alkalosis" and acid_base_status == "Alkalosis":
        # Check for respiratory compensation in metabolic alkalosis
        expected_pco2 = 0.7 * bicarbonate + 20
        if pco2 < (expected_pco2 - 5):
            respiratory_compensation = "Inadequate compensation"
        elif pco2 > (expected_pco2 + 5):
            respiratory_compensation = (
                "Excessive compensation (concomitant respiratory acidosis)"
            )
        else:
            respiratory_compensation = "Adequate compensation"
    else:
        respiratory_compensation = "Not applicable"

    if gap_type == "High Anion Gap Metabolic Acidosis (HAGMA)":
        delta_ratio = (anion_gap - 12) / (24 - bicarbonate)
        if delta_ratio < 0.4:
            concomitant_disorder = "Normal Anion Gap Metabolic Acidosis (NAGMA)"
        elif 0.4 <= delta_ratio <= 0.8:
            concomitant_disorder = "Mixed Disorder (NAGMA + HAGMA)"
        elif 1 <= delta_ratio <= 2:
            concomitant_disorder = "Pure High Anion Gap Metabolic Acidosis (HAGMA)"
        elif delta_ratio > 2:
            concomitant_disorder = "Mixed Disorder (HAGMA + Metabolic Alkalosis or Chronic Respiratory Acidosis)"
        else:
            concomitant_disorder = "Not applicable"

    if gap_type == "High Anion Gap Metabolic Acidosis (HAGMA)":
        # Calculate osmolal gap in HAGMA
        osmolal_gap = measured_serum_osmolality - 2 * (sodium) - (urea + glucose)
    else:
        concomitant_disorder = "Not applicable"
        osmolal_gap = None

    result = {
        "Acid-Base Status": acid_base_status,
        "Cause": cause,
        "Anion Gap Type": gap_type,
        "Concomitant Disorder": concomitant_disorder,
        "Respiratory Compensation": respiratory_compensation,
        "Expected Change in HCO3- (Acute)": expected_change_acute,
        "Expected Change in HCO3- (Chronic)": expected_change_chronic,
        "Osmolal Gap": osmolal_gap,
    }
    return result


def main():
    try:
        ph_input = float(input("Enter the pH value: "))
        pco2_input = float(input("Enter the pCO2 value: "))
        bicarbonate_input = float(input("Enter the bicarbonate value: "))
        sodium_input = float(input("Enter the sodium value: "))
        chloride_input = float(input("Enter the chloride value: "))
        measured_serum_osmolality_input = float(
            input("Enter the measured serum osmolality: ")
        )
        glucose_input = float(input("Enter the glucose value: "))
        urea_input = float(input("Enter the urea value: "))

        result = determine_acid_base_balance(
            ph_input,
            pco2_input,
            bicarbonate_input,
            sodium_input,
            chloride_input,
            measured_serum_osmolality_input,
            glucose_input,
            urea_input,
        )
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")


if __name__ == "__main__":
    main()
