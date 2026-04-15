import json
import math

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees) in Kilometers.
    """
    R = 6371  # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# 1. Load the data
with open('drc_floods.json', 'r') as f:
    floods = json.load(f)

with open('drc_health_infrastructure.json', 'r') as f:
    health_data = json.load(f)

sites_at_risk = []
risk_threshold_km = 1.0  # 1km distance

# 2. Compare every health site to every flood location
for site in health_data['elements']:
    site_lat = site.get('lat') or (site.get('center', {}).get('lat'))
    site_lon = site.get('lon') or (site.get('center', {}).get('lon'))
    
    if not site_lat or not site_lon:
        continue

    is_at_risk = False
    nearest_flood_dist = float('inf')
    flood_info = ""

    for flood in floods:
        f_lat = flood.get('lat')
        f_lon = flood.get('long')
        
        if f_lat and f_lon:
            dist = haversine(site_lat, site_lon, f_lat, f_lon)
            if dist <= risk_threshold_km:
                is_at_risk = True
                if dist < nearest_flood_dist:
                    nearest_flood_dist = dist
                    flood_info = f"Flood Date: {flood.get('Began', 'Unknown')}"

    if is_at_risk:
        # Add risk info to the site tags
        if 'tags' not in site: site['tags'] = {}
        site['tags']['risk_level'] = "HIGH"
        site['tags']['distance_to_flood'] = round(nearest_flood_dist, 3)
        site['tags']['flood_event'] = flood_info
        sites_at_risk.append(site)

# 3. Save the specific at-risk sites to a small file
with open('sites_at_risk.json', 'w') as f:
    json.dump({"elements": sites_at_risk}, f)

print(f"Analysis complete! Found {len(sites_at_risk)} health sites within 1km of a flood.")
print("Saved to 'sites_at_risk.json'.")
