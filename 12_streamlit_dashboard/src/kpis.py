from read_data import read_data

df = read_data()

approved = df.query("Beslut == 'Beviljad'")
number_approved = len(approved)
total_applications = len(df)
approved_percentage = f"{number_approved / total_applications * 100:.1f} %"
number_distance = len(df.query("Studieform == 'Distans'"))
approved_remote = len(approved.query("Studieform == 'Distans'"))


def provider_kpis(provider):
    applied = df.query(f"`Utbildningsanordnare administrativ enhet` == '{provider}'")
    applications = len(applied)
    approved_applications = len(applied.query("Beslut == 'Beviljad'"))

    return applications, approved_applications