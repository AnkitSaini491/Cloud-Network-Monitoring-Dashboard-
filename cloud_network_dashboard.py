
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# CLOUD NETWORK MONITORING DATA
# ==========================================

cloud = {
    "Month": [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ],

    "Network_Traffic": [
        420, 450, 480, 510, 545, 580,
        620, 660, 705, 750, 800, 850
    ],

    "Active_Instances": [
        120, 128, 135, 142, 150, 158,
        166, 175, 184, 193, 202, 215
    ],

    "Latency": [
        42, 41, 40, 39, 41, 38,
        37, 36, 38, 35, 34, 33
    ],

    "Failed_Requests": [
        420, 405, 390, 370, 360, 345,
        330, 315, 300, 285, 270, 255
    ],

    "Bandwidth": [
        65, 68, 71, 74, 78, 81,
        84, 87, 90, 93, 96, 99
    ],

    "Availability": [
        98.9, 99.0, 99.1, 99.2, 99.1, 99.3,
        99.4, 99.5, 99.4, 99.6, 99.7, 99.8
    ]
}

df = pd.DataFrame(cloud)

# ==========================================
# KPI CALCULATIONS
# ==========================================

total_traffic = df["Network_Traffic"].sum()
total_instances = df["Active_Instances"].sum()
avg_latency = df["Latency"].mean()
total_failed = df["Failed_Requests"].sum()
avg_bandwidth = df["Bandwidth"].mean()
avg_availability = df["Availability"].mean()

# ==========================================
# DASHBOARD SETUP
# ==========================================

plt.style.use("dark_background")

fig = plt.figure(figsize=(20, 12))
fig.patch.set_facecolor("#081421")

fig.suptitle(
    "CLOUD NETWORK MONITORING DASHBOARD",
    fontsize=28,
    fontweight="bold",
    color="white"
)

# ==========================================
# KPI CARDS
# ==========================================

plt.figtext(
    0.03, 0.90,
    f"Network Traffic\n{total_traffic:,} GB",
    fontsize=14,
    bbox=dict(facecolor="#2563EB", boxstyle="round,pad=0.8")
)

plt.figtext(
    0.20, 0.90,
    f"Active Instances\n{total_instances:,}",
    fontsize=14,
    bbox=dict(facecolor="#16A34A", boxstyle="round,pad=0.8")
)

plt.figtext(
    0.38, 0.90,
    f"Avg Latency\n{avg_latency:.1f} ms",
    fontsize=14,
    bbox=dict(facecolor="#F59E0B", boxstyle="round,pad=0.8")
)

plt.figtext(
    0.56, 0.90,
    f"Failed Requests\n{total_failed:,}",
    fontsize=14,
    bbox=dict(facecolor="#DC2626", boxstyle="round,pad=0.8")
)

plt.figtext(
    0.74, 0.90,
    f"Bandwidth\n{avg_bandwidth:.1f}%",
    fontsize=14,
    bbox=dict(facecolor="#8B5CF6", boxstyle="round,pad=0.8")
)

plt.figtext(
    0.89, 0.90,
    f"Availability\n{avg_availability:.2f}%",
    fontsize=14,
    bbox=dict(facecolor="#06B6D4", boxstyle="round,pad=0.8")
)

# ==========================================
# CHART 1 - NETWORK TRAFFIC TREND
# ==========================================

ax1 = plt.subplot(3, 2, 1)

ax1.plot(
    df["Month"],
    df["Network_Traffic"],
    marker="o",
    linewidth=3,
    color="cyan"
)

ax1.fill_between(
    df["Month"],
    df["Network_Traffic"],
    alpha=0.25
)

ax1.set_title("Monthly Network Traffic")
ax1.set_xlabel("Month")
ax1.set_ylabel("Traffic (GB)")
ax1.grid(alpha=0.3)

ax1.tick_params(axis="x", rotation=45)

# ==========================================
# SHOW DASHBOARD
# ==========================================

plt.tight_layout(rect=[0, 0, 1, 0.87])

plt.show()
# ==========================================
# CHART 2 - LATENCY TREND
# ==========================================

ax2 = plt.subplot(3, 2, 2)

ax2.plot(
    df["Month"],
    df["Latency"],
    marker="o",
    linewidth=3,
    color="orange"
)

ax2.fill_between(
    df["Month"],
    df["Latency"],
    alpha=0.25
)

ax2.set_title("Average Network Latency")
ax2.set_xlabel("Month")
ax2.set_ylabel("Latency (ms)")
ax2.grid(alpha=0.3)

ax2.tick_params(axis="x", rotation=45)


# ==========================================
# CHART 3 - ACTIVE CLOUD INSTANCES
# ==========================================

ax3 = plt.subplot(3, 2, 3)

ax3.bar(
    df["Month"],
    df["Active_Instances"]
)

ax3.set_title("Active Cloud Instances")
ax3.set_xlabel("Month")
ax3.set_ylabel("Instances")
ax3.grid(alpha=0.3)

ax3.tick_params(axis="x", rotation=45)


# ==========================================
# CHART 4 - FAILED REQUESTS
# ==========================================

ax4 = plt.subplot(3, 2, 4)

ax4.plot(
    df["Month"],
    df["Failed_Requests"],
    marker="o",
    linewidth=3,
    color="red"
)

ax4.fill_between(
    df["Month"],
    df["Failed_Requests"],
    alpha=0.25
)

ax4.set_title("Failed Network Requests")
ax4.set_xlabel("Month")
ax4.set_ylabel("Failed Requests")
ax4.grid(alpha=0.3)

ax4.tick_params(axis="x", rotation=45)


# ==========================================
# CHART 5 - BANDWIDTH USAGE
# ==========================================

ax5 = plt.subplot(3, 2, 5)

ax5.plot(
    df["Month"],
    df["Bandwidth"],
    marker="o",
    linewidth=3,
    color="lime"
)

ax5.fill_between(
    df["Month"],
    df["Bandwidth"],
    alpha=0.25
)

ax5.set_title("Bandwidth Utilization")
ax5.set_xlabel("Month")
ax5.set_ylabel("Utilization (%)")
ax5.set_ylim(0, 110)
ax5.grid(alpha=0.3)

ax5.tick_params(axis="x", rotation=45)


# ==========================================
# CHART 6 - REGION-WISE NETWORK TRAFFIC
# ==========================================

region = pd.DataFrame({

    "Region": [
        "North",
        "South",
        "East",
        "West",
        "Central"
    ],

    "Traffic": [
        185,
        225,
        150,
        205,
        125
    ]
})

# New figure for regional analysis
plt.figure(figsize=(10, 5))

plt.bar(
    region["Region"],
    region["Traffic"]
)

plt.title("Region-wise Network Traffic")
plt.xlabel("Region")
plt.ylabel("Traffic (GB)")
plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()
# ==========================================
# CHART 7 - PROTOCOL DISTRIBUTION
# ==========================================

protocol = pd.DataFrame({
    "Protocol": ["HTTPS", "HTTP", "TCP", "UDP", "ICMP"],
    "Traffic": [42, 18, 20, 13, 7]
})

plt.figure(figsize=(9, 6))

plt.pie(
    protocol["Traffic"],
    labels=protocol["Protocol"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Cloud Network Protocol Distribution")

plt.tight_layout()
plt.show()


# ==========================================
# CHART 8 - SERVER CPU USAGE
# ==========================================

cpu = pd.DataFrame({
    "Month": df["Month"],
    "CPU_Usage": [
        45, 48, 51, 49, 53, 56,
        58, 61, 59, 63, 66, 69
    ]
})

plt.figure(figsize=(10, 5))

plt.plot(
    cpu["Month"],
    cpu["CPU_Usage"],
    marker="o",
    linewidth=3
)

plt.title("Cloud Server CPU Usage")
plt.xlabel("Month")
plt.ylabel("CPU Usage (%)")
plt.ylim(0, 100)
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()


# ==========================================
# CHART 9 - MEMORY USAGE
# ==========================================

memory = pd.DataFrame({
    "Month": df["Month"],
    "Memory_Usage": [
        52, 54, 56, 55, 58, 60,
        62, 64, 63, 66, 68, 71
    ]
})

plt.figure(figsize=(10, 5))

plt.plot(
    memory["Month"],
    memory["Memory_Usage"],
    marker="o",
    linewidth=3
)

plt.title("Cloud Memory Utilization")
plt.xlabel("Month")
plt.ylabel("Memory Usage (%)")
plt.ylim(0, 100)
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()


# ==========================================
# CHART 10 - NETWORK AVAILABILITY
# ==========================================

plt.figure(figsize=(10, 5))

plt.plot(
    df["Month"],
    df["Availability"],
    marker="o",
    linewidth=3
)

plt.title("Network Availability Trend")
plt.xlabel("Month")
plt.ylabel("Availability (%)")
plt.ylim(95, 100)
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()


# ==========================================
# CLOUD MONITORING SUMMARY
# ==========================================

best_availability = df.loc[
    df["Availability"].idxmax()
]

lowest_latency = df.loc[
    df["Latency"].idxmin()
]

highest_traffic = df.loc[
    df["Network_Traffic"].idxmax()
]

print("=" * 70)
print("CLOUD NETWORK MONITORING SUMMARY")
print("=" * 70)

print(f"Total Network Traffic : {total_traffic:,} GB")
print(f"Total Cloud Instances : {total_instances:,}")
print(f"Average Latency       : {avg_latency:.2f} ms")
print(f"Failed Requests       : {total_failed:,}")
print(f"Average Bandwidth     : {avg_bandwidth:.2f}%")
print(f"Network Availability  : {avg_availability:.2f}%")

print("\nPERFORMANCE INSIGHTS")
print("-" * 70)

print(
    f"Highest Traffic Month : "
    f"{highest_traffic['Month']} "
    f"({highest_traffic['Network_Traffic']} GB)"
)

print(
    f"Lowest Latency Month  : "
    f"{lowest_latency['Month']} "
    f"({lowest_latency['Latency']} ms)"
)

print(
    f"Best Availability     : "
    f"{best_availability['Month']} "
    f"({best_availability['Availability']}%)"
)

print("=" * 70)


# ==========================================
# SAVE MAIN DASHBOARD
# ==========================================

fig.savefig(
    "cloud_network_monitoring_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

print(
    "\nDashboard saved as "
    "cloud_network_monitoring_dashboard.png"
)


# ==========================================
# PROJECT INFORMATION
# ==========================================

print("\nPROJECT INFORMATION")
print("-" * 70)

print("Project  : Cloud Network Monitoring Dashboard")
print("Tools    : Python | Pandas | Matplotlib")
print("Domain   : Cloud & Network Analytics")
print("Purpose  : Cloud infrastructure monitoring")
print("Status   : Dashboard Generated Successfully")


# ==========================================
# FOOTER
# ==========================================

plt.figtext(
    0.25,
    0.02,
    "Cloud Network Monitoring | Python | Pandas | Matplotlib",
    fontsize=11
)

plt.show()
