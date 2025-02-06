import allure
from xmlschema import XMLSchemaChildrenValidationError

from templates.read_templates import country_iso_code_xml, xsd_response, country_name_xml
import xml.etree.ElementTree as ET

from templates.xml_parser import dictify


@allure.feature('SOAP')
class TestPeople:
    @allure.story('Positive tests')
    class TestPositive:

        def test_country_name_service(self, soap_session):
            response = soap_session.request(method='POST', data=country_iso_code_xml('IT'))
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/soap+xml; charset=utf-8'

            try:
                xsd_response('CountryNameResponse').validate(response.text)
            except XMLSchemaChildrenValidationError as xml_e:
                raise AssertionError(xml_e)

            root = ET.fromstring(response.text)
            assert root[0][0][0].text == 'Italy'
            assert 'CountryNameResult' in root[0][0][0].tag

            pass
            # assert country_iso_code_xsd_response.is_valid(response.text)

        def test_country_iso_service(self, soap_session):
            response = soap_session.request(method='POST', data=country_name_xml('Italy'))
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/soap+xml; charset=utf-8'

            try:
                xsd_response('CountryISOCodeResponse').validate(response.text)
            except XMLSchemaChildrenValidationError as xml_e:
                raise AssertionError(xml_e)

            root = ET.fromstring(response.text)
            assert root[0][0][0].text == 'IT'
