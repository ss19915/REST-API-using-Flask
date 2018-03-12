			--------------REST API to get Capitals of various Country------------
      
	The REST API can return name of county and its capital in json format of the given country.To get capital of desired country apped /capital/<countryName> at the end of domain name.
Eg:- let say the domain name is abc.ngrok.io and we want capital of India . So the link for that would be "abc.ngrok.io/capital/india" and response to this http get request will be
{
  "CAPITAL": "NEW DELHI",
  "COUNTRY": "INDIA"
}
