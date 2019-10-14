

def get_current_channel_planning(mist_session, site_id):
    uri = "/api/v1/sites/%s/rrm/current" % site_id
    resp = mist_session.mist_get(uri, site_id=site_id)
    return resp

def get_device_rrm_info(mist_session, site_id, device_id, band):
    uri = "/api/v1/sites/%s/rrm/current/devices/%s/band/%s" % (site_id, device_id, band)
    resp = mist_session.mist_get(uri,site_id=site_id)
    return resp

def optimize(mist_session, site_id, band_24=False, band_5=False):
    bands = []
    if band_24:
        bands.append("24")
    if band_5:
        bands.append("5")
    body = { "bands": bands}
    uri = "/api/v1/sites/%s/rrm/optimize" % site_id
    resp = mist_session.mist_post(uri, site_id=site_id, body=body)
    return resp

def reset(mist_session, site_id):
    uri = "/api/v1/sites/%s/devices/reset_radio_config" % site_id
    resp = mist_session.mist_post(uri, site_id=site_id)
    return resp

def get_events(mist_session, site_id, band, limit="", duration=""):
    uri ="/api/v1/sites/%s/rrm/events?band=%s" % (site_id, band)
    if limit != "":
        uri += "&limit=%s" % limit
    if duration != "":
        uri += "&duration=%s" % duration
    resp = mist_session.mist_get(uri, site_id=site_id)
    return resp

def get_interference_events(mist_session, site_id, limit="", page=1, duration=""):
    uri = "/api/v1/sites/%s/events/interference?page=%s" % (site_id, page)
    if limit != "":
        uri += "&limit=%s" % limit
    if duration != duration:
        uri += "&duration=%s" %duration
    resp = mist_session.mist_get(uri, site_id=site_id)
    return resp

def get_roaming_events(mist_session, site_id, mtype, start="", end="", limit=""):
    uri = "/api/v1/sites/%s/events/fast_roam?type=%s" % (site_id, mtype)
    if start != "":
        uri += "&limit=%s" % start
    if end != "":
        uri += "&duration=%s" % end
    if limit != "":
        uri += "&duration=%s" % limit
    resp = mist_session.mist_get(uri, site_id=site_id)
    return resp
