from read_data import read_data

df= read_data()

# 被批准的课程
approved = df.query("Beslut == 'Beviljad'")
number_approved = len(approved)
total_applications = len(df)
approved_percentage = f"{number_approved / total_applications*100:.1f}%"

def provider_kpis(provider):
    applied = df.query(f"`Utbildningsanordnare administrativ enhet` == '{provider}'")
    applications = len(applied)
    approved = len(applied.query("Beslut == 'Beviljad'"))
    
    return applications, approved

print(provider_kpis("Futuregames Umeå"))



















