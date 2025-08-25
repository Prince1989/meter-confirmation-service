from datetime import datetime, timezone

def _iso_now():
    # Match sample with timezone offset (South Africa is UTC+02:00); produce ISO with offset if available
    return datetime.now().astimezone().isoformat()

def soap_fault_invalid_format():
    return """<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <soap:Fault>
      <faultcode>soap:Client</faultcode>
      <faultstring>Invalid meter number format</faultstring>
    </soap:Fault>
  </soap:Body>
</soap:Envelope>
"""

def soap_fault_meter_info():
    return f"""<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <soap:Body>
    <soap:Fault>
      <faultcode>soap:Server</faultcode>
      <faultstring>010038 Meter information not found</faultstring>
      <faultactor>http://onlinevending.eskom.co.za/OVS/WS/Actaris.WSNRS21EskomFull/WSActaris.asmx</faultactor>
      <detail>
        <b0:xmlvendFaultResp xmlns:r0="http://www.nrs.eskom.co.za/xmlvend/revenue/2.1/schema"
                             xmlns:b0="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema">
          <b0:clientID xsi:type="b0:GenericDeviceID" id="6004708000090"/>
          <b0:serverID xsi:type="b0:EANDeviceID" ean="0123123456789"/>
          <b0:terminalID xsi:type="b0:GenericDeviceID" id="6004708000090"/>
          <b0:reqMsgID dateTime="22222222222222222" uniqueNumber="2222222"/>
          <b0:respDateTime>{_iso_now()}</b0:respDateTime>
          <b0:dispHeader>ONLINE ERROR</b0:dispHeader>
          <b0:operatorMsg>Meter information not found,cannot process request. Contact Eskom to register meter</b0:operatorMsg>
          <b0:custMsg>Meter not found.Contact Eskom to register meter</b0:custMsg>
          <b0:fault xsi:type="b0:UnknownMeterEx">
            <b0:desc>010038 Meter information not found</b0:desc>
          </b0:fault>
        </b0:xmlvendFaultResp>
      </detail>
    </soap:Fault>
  </soap:Body>
</soap:Envelope>
"""

def soap_not_found_response():
    return """<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <confirmMeterResp>
      <message>Meter not Found</message>
    </confirmMeterResp>
  </soap:Body>
</soap:Envelope>
"""

def soap_success_response(msno: str):
    return f"""<?xml version='1.0' encoding='UTF-8'?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <soap:Body>
    <confirmMeterResp xmlns:b0="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema"
                      xmlns:r0="http://www.nrs.eskom.co.za/xmlvend/revenue/2.1/schema"
                      xmlns="http://www.nrs.eskom.co.za/xmlvend/meter/2.1/schema">
      <b0:clientID xsi:type="b0:GenericDeviceID" id="6004708000090"/>
      <b0:serverID xsi:type="b0:EANDeviceID" ean="0123123456789"/>
      <b0:terminalID xsi:type="b0:GenericDeviceID" id="6004708000090"/>
      <b0:reqMsgID dateTime="22222222222222222" uniqueNumber="2222222"/>
      <b0:respDateTime>{_iso_now()}</b0:respDateTime>
      <b0:dispHeader>Confirm Meter Details</b0:dispHeader>
      <confirmMeterResult>
        <meterDetail xsi:type="b0:ExtMeterDetail" msno="{msno}" sgc="100836" krn="2" ti="07">
          <b0:meterType at="07" tt="02"/>
        </meterDetail>
      </confirmMeterResult>
    </confirmMeterResp>
  </soap:Body>
</soap:Envelope>
"""
