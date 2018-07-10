"""
Fetches students of a college based on roll no of one student.
"""

# roll no of a college student

import requests
from bs4 import BeautifulSoup



CONST_VIEWSTATE = """/wEPDwUJMjIwMjE3NzMyD2QWAgIDD2QWFgIBD2QWAgIFDw8WAh4EVGV4dAUzUmVzdWx0cyAoMy1ZZWFyIFNlbWVzdGVyIEV4YW1pbmF0aW9uIE5vdi1EZWMgMjAxNyApZGQCBQ8PFgIfAAUPIChOb3YtRGVjIDIwMTcpZGQCCw8PFgQeB1Zpc2libGVnHwAFF1NvcnJ5ISBubyByZWNvcmQgZm91bmQuZGQCEQ8QDxYGHg1EYXRhVGV4dEZpZWxkBQlDT0xMX05BTUUeDkRhdGFWYWx1ZUZpZWxkBQlDT0xMX0NPREUeC18hRGF0YUJvdW5kZ2QQFVESPC0tLS0tU2VsZWN0LS0tLS0+IkFjaGFyeWEgTmFyZW5kcmEgRGV2IENvbGxlZ2UtKDAwMSkZQWRpdGkgTWFoYXZpZHlhbGF5YS0oMDAyKUNBcnlhYmhhdHRhIENvbGxlZ2UgW0Zvcm1lcmx5IFJhbSBMYWwgQW5hbmQgQ29sbGVnZSAoRXZlbmluZyldLSgwNTkpJUF0bWEgUmFtIFNhbmF0YW4gRGhhcmFtIENvbGxlZ2UtKDAwMykeQmhhZ2luaSBOaXZlZGl0YSBDb2xsZWdlLSgwMDcpFUJoYXJhdGkgQ29sbGVnZS0oMDA4KTBCaGFza2FyYWNoYXJ5YSBDb2xsZWdlIG9mIEFwcGxpZWQgU2NpZW5jZXMtKDAwOSkXQ0FNUFVTIExBVyBDRU5UUkUtKDMwOSkfQ2x1c3RlciBJbm5vdmF0aW9uIENlbnRyZS0oMzEyKSNDb2xsZWdlIE9mIFZvY2F0aW9uYWwgU3R1ZGllcy0oMDEzKRhEYXVsYXQgUmFtIENvbGxlZ2UtKDAxNCkiRGVlbiBEYXlhbCBVcGFkaHlheWEgQ29sbGVnZS0oMDE1KSZEZWxoaSBDb2xsZWdlIE9mIEFydHMgJiBDb21tZXJjZS0oMDE2KSBEZWxoaSBTY2hvb2wgb2YgSm91cm5hbGlzbS0oMzE2KXhEZXBhcnRtZW50IG9mIENvbXB1dGVyIFNjaWVuY2UgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAtKDIzNCkdRGVwYXJ0bWVudCBvZiBFZHVjYXRpb24tKDI0MykdRGVwYXJ0bWVudCBvZiBHZW9ncmFwaHktKDIyOSkwRGVwYXJ0bWVudCBvZiBHZXJtYW5pYyBhbmQgUm9tYW5jZSBTdHVkaWVzLSgyMDQpM0RlcGFydG1lbnQgb2YgTGlicmFyeSBhbmQgSW5mb3JtYXRpb24gU2NpZW5jZS0oMjA2KRlEZXBhcnRtZW50IG9mIE11c2ljLSgyNDApHkRlc2hiYW5kaHUgQ29sbGVnZSAoRGF5KS0oMDE5KSNEci4gQmhpbSBSYW8gQW1iZWRrYXIgQ29sbGVnZS0oMDEwKUhEdXJnYWJhaSBEZXNobXVraCBDb2xsZWdlIG9mIFNwZWNpYWwgRWR1Y2F0aW9uIChWaXN1YWwgSW1wYWlybWVudCktKDMxNCkeRHlhbCBTaW5naCBDb2xsZWdlIChEYXkpLSgwMjEpHkR5YWwgU2luZ2ggQ29sbGVnZSAoRXZlKS0oMDIyKSNGYWN1bHR5IG9mIE1hbmFnZW1lbnQgU3R1ZGllcy0oMTA5KRNHYXJnaSBDb2xsZWdlLSgwMjQpFkhhbnMgUmFqIENvbGxlZ2UtKDAyNSkTSGluZHUgQ29sbGVnZS0oMDI2KRtJLlAuQ29sbGVnZSBGb3IgV29tZW4tKDAyOSk8SW5kaXJhIEdhbmRoaSBJbnN0aXR1dGUgb2YgUGh5LiBFZHUuICYgU3BvcnRzIFNjaWVuY2VzLSgwMjgpIUluc3RpdHV0ZSBPZiBIb21lIEVjb25vbWljcy0oMDMwKSFKYW5raSBEZXZpIE1lbW9yaWFsIENvbGxlZ2UtKDAzMSkaSmVzdXMgJiBNYXJ5IENvbGxlZ2UtKDAzMikVS2FsaW5kaSBDb2xsZWdlLSgwMzMpGUthbWxhIE5laHJ1IENvbGxlZ2UtKDAzNCkaS2VzaGF2IE1haGF2aWR5YWxheWEtKDAzNSkYS2lyb3JpIE1hbCBDb2xsZWdlLSgwMzYpGExhZHkgSXJ3aW4gQ29sbGVnZS0oMDM4KSRMYWR5IFNyaSBSYW0gQ29sbGVnZSBGb3IgV29tZW4tKDAzOSkYTGFrc2htaWJhaSBDb2xsZWdlLSgwNDApEkxBVyBDRU5UUkUtSS0oMzEwKRNMQVcgQ0VOVFJFLUlJLSgzMTEpHk1haGFyYWphIEFncmFzZW4gQ29sbGVnZS0oMDQxKStNYWhhcnNoaSBWYWxtaWtpIENvbGxlZ2Ugb2YgRWR1Y2F0aW9uLSgzMTUpFk1haXRyZXlpIENvbGxlZ2UtKDA0MykjTWF0YSBTdW5kcmkgQ29sbGVnZSBGb3IgV29tZW4tKDA0NCkTTWlyYW5kYSBIb3VzZS0oMDQ3KSJNb3RpIExhbCBOZWhydSBDb2xsZWdlIChEYXkpLSgwNDgpIk1vdGkgTGFsIE5laHJ1IENvbGxlZ2UgKEV2ZSktKDA0OSkeUC5HLkQuQS5WLiBDb2xsZWdlIChEYXkpLSgwNTMpHlAuRy5ELkEuVi4gQ29sbGVnZSAoRXZlKS0oMDU0KRZSYWpkaGFuaSBDb2xsZWdlLSgwNTUpIVJhbSBMYWwgQW5hbmQgQ29sbGVnZSAoRGF5KS0oMDU4KRdSYW1hbnVqYW4gQ29sbGVnZS0oMDIwKRRSYW1qYXMgQ29sbGVnZS0oMDU2KR1TLkcuVC5CLiBLaGFsc2EgQ29sbGVnZS0oMDY4KR1TYXR5YXdhdGkgQ29sbGVnZSAoRGF5KS0oMDYyKR1TYXR5YXdhdGkgQ29sbGVnZSAoRXZlKS0oMDYzKR1TY2hvb2wgb2YgT3BlbiBMZWFybmluZy0oU09MKShTaGFoZWVkIEJoYWdhdCBTaW5naCBDb2xsZWdlIChEYXkpLSgwNjQpKFNoYWhlZWQgQmhhZ2F0IFNpbmdoIENvbGxlZ2UgKEV2ZSktKDA2NSk7U2hhaGVlZCBSYWpndXJ1IENvbGxlZ2Ugb2YgQXBwbGllZCBTY2llbmNlcyBmb3IgV29tZW4tKDA2NikxU2hhaGVlZCBTdWtoZGV2IENvbGxlZ2Ugb2YgQnVzaW5lc3MgU3R1ZGllcy0oMDY3KRVTaGl2YWppIENvbGxlZ2UtKDA3MSkdU2h5YW0gTGFsIENvbGxlZ2UgKERheSktKDA3MykdU2h5YW0gTGFsIENvbGxlZ2UgKEV2ZSktKDA3NCklU2h5YW1hIFByYXNhZCBNdWtoZXJqZWUgQ29sbGVnZS0oMDc1KSFTcmkgQXVyb2JpbmRvIENvbGxlZ2UgKERheSktKDA3NikhU3JpIEF1cm9iaW5kbyBDb2xsZWdlIChFdmUpLSgwNzcpL1NyaSBHdXJ1IEdvYmluZCBTaW5naCBDb2xsZWdlIE9mIENvbW1lcmNlLSgwNzgpJ1NyaSBHdXJ1IE5hbmFrIERldiBLaGFsc2EgQ29sbGVnZS0oMDY5KSFTcmkgUmFtIENvbGxlZ2UgT2YgQ29tbWVyY2UtKDA3MikeU3JpIFZlbmthdGVzd2FyYSBDb2xsZWdlLSgwNzkpGlN0LiBTdGVwaGVucyBDb2xsZWdlLSgwODApIFN3YW1pIFNocmFkZGhhbmFuZCBDb2xsZWdlLSgwODEpGVVuaXZlcnNpdHkgb2YgRGVsaGktKDEwMCkZVml2ZWthbmFuZGEgQ29sbGVnZS0oMDg0KSBaYWtpciBIdXNhaW4gQ29sbGVnZSAoRXZlKS0oMDg2KSZaYWtpciBIdXNhaW4gRGVsaGkgQ29sbGVnZSAoRGF5KS0oMDg1KRVREjwtLS0tLVNlbGVjdC0tLS0tPgMwMDEDMDAyAzA1OQMwMDMDMDA3AzAwOAMwMDkDMzA5AzMxMgMwMTMDMDE0AzAxNQMwMTYDMzE2AzIzNAMyNDMDMjI5AzIwNAMyMDYDMjQwAzAxOQMwMTADMzE0AzAyMQMwMjIDMTA5AzAyNAMwMjUDMDI2AzAyOQMwMjgDMDMwAzAzMQMwMzIDMDMzAzAzNAMwMzUDMDM2AzAzOAMwMzkDMDQwAzMxMAMzMTEDMDQxAzMxNQMwNDMDMDQ0AzA0NwMwNDgDMDQ5AzA1MwMwNTQDMDU1AzA1OAMwMjADMDU2AzA2OAMwNjIDMDYzA1NPTAMwNjQDMDY1AzA2NgMwNjcDMDcxAzA3MwMwNzQDMDc1AzA3NgMwNzcDMDc4AzA2OQMwNzIDMDc5AzA4MAMwODEDMTAwAzA4NAMwODYDMDg1FCsDUWdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAhkPEGRkFgECAWQCIQ8QDxYGHwIFCUVYQU1fRkxBRx8DBQlFWEFNX0ZMQUcfBGdkEBUFEzwtLS0tLVNlbGVlY3QtLS0tLT4EQ0JDUw5VR19TRU1FU1RFUl8zWQ5VR19TRU1FU1RFUl80WQ5QR19TRU1FU1RFUl8yWRUFEzwtLS0tLVNlbGVlY3QtLS0tLT4EQ0JDUw5VR19TRU1FU1RFUl8zWQ5VR19TRU1FU1RFUl80WQ5QR19TRU1FU1RFUl8yWRQrAwVnZ2dnZxYBAgFkAikPEGRkFgECAmQCMQ8QDxYGHwIFC0NPVVJTRV9OQU1FHwMFC0NPVVJTRV9DT0RFHwRnZBAVHBI8LS0tLS1TZWxlY3QtLS0tLT4nKENCQ1MpIEIuUC5FRC4gVFdPIFlFQVIgUFJPR1JBTU1FLSg1OTUpQShDQkNTKSBCLlNjLiAoUEhZU0lDQUwgRURVQ0FUSU9OLEhFQUxUSCBFRFVDQVRJT04gJiBTUE9SVFMpLSg1ODkpJyhDQkNTKSBCLlNDLiBBTkFMWVRJQ0FMIENIRU1JU1RSWS0oNTg1KVAoQ0JDUykgQi5TQy4gQVBQTElFRCBMSUZFIFNDSUVOQ0VTIFdJVEggQUdSTy1DSEVNSUNBTFMgQU5EIFBFU1QgTUFOQUdFTUVOVC0oNTg2KScoQ0JDUykgQi5TQy4gSU5EVVNUUklBTCBDSEVNSVNUUlktKDU4NCkfKENCQ1MpIEIuU0MuIExJRkUgU0NJRU5DRS0oNTgzKSMoQ0JDUykgQi5TQy4gUEhZU0lDQUwgU0NJRU5DRS0oNTgyKSYoQ0JDUykgQi5TQy4oSE9OUy4pIEFOVEhST1BPTE9HWS0oNTUxKSYoQ0JDUykgQi5TQy4oSE9OUy4pIEJJT0NIRU1JU1RSWS0oNTUzKS0oQ0JDUykgQi5TQy4oSE9OUy4pIEJJT0xPR0lDQUwgU0NJRU5DRSAtKDU1NSktKENCQ1MpIEIuU0MuKEhPTlMuKSBCSU9NRURJQ0FMIFNDSUVOQ0VTLSg1NTQpIChDQkNTKSBCLlNDLihIT05TLikgQk9UQU5ZLSg1NTYpJChDQkNTKSBCLlNDLihIT05TLikgQ0hFTUlTVFJZIC0oNTU3KSooQ0JDUykgQi5TQy4oSE9OUy4pIENPTVBVVEVSIFNDSUVOQ0UtKDU3MCksKENCQ1MpIEIuU0MuKEhPTlMuKSBFTEVDVFJPTklDIFNDSUVOQ0UtKDU1OCkpKENCQ1MpIEIuU0MuKEhPTlMuKSBGT09EIFRFQ0hOT0xPR1ktKDU1OSkhKENCQ1MpIEIuU0MuKEhPTlMuKSBHRU9MT0dZLSg1NjApJihDQkNTKSBCLlNDLihIT05TLikgSE9NRSBTQ0lFTkNFLSg1NjEpKShDQkNTKSBCLlNDLihIT05TLikgSU5TVFJVTUVOVEFUSU9OLSg1NjIpJShDQkNTKSBCLlNDLihIT05TLikgTUFUSEVNQVRJQ1MtKDU2MykmKENCQ1MpIEIuU0MuKEhPTlMuKSBNSUNST0JJT0xPR1ktKDU2NCkiKENCQ1MpIEIuU0MuKEhPTlMuKSBQSFlTSUNTIC0oNTY3KSkoQ0JDUykgQi5TQy4oSE9OUy4pIFBPTFlNRVIgU0NJRU5DRS0oNTY2KSQoQ0JDUykgQi5TQy4oSE9OUy4pIFNUQVRJU1RJQ1MtKDU2OCkhKENCQ1MpIEIuU0MuKEhPTlMuKSBaT09MT0dZLSg1NjkpJShDQkNTKSBCLlNDLihQQVNTKSBIT01FIFNDSUVOQ0UtKDU5MSkqKENCQ1MpLUIuU0MuIChNQVRIRU1BVElDQUwgU0NJRU5DRVMpLSg1ODcpFRwSPC0tLS0tU2VsZWN0LS0tLS0+AzU5NQM1ODkDNTg1AzU4NgM1ODQDNTgzAzU4MgM1NTEDNTUzAzU1NQM1NTQDNTU2AzU1NwM1NzADNTU4AzU1OQM1NjADNTYxAzU2MgM1NjMDNTY0AzU2NwM1NjYDNTY4AzU2OQM1OTEDNTg3FCsDHGdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2cWAQIOZAI5DxAPFgYfAgUEUEFSVB8DBQRQQVJUHwRnZBAVBRI8LS0tLS1TZWxlY3QtLS0tLT4BSQJJSQNJSUkCSVYVBRI8LS0tLS1TZWxlY3QtLS0tLT4BSQJJSQNJSUkCSVYUKwMFZ2dnZ2cWAQIBZAI/DxAPFgYfAgUDU0VNHwMFA1NFTR8EZ2QQFQMSPC0tLS0tU2VsZWN0LS0tLS0+AUkCSUkVAxI8LS0tLS1TZWxlY3QtLS0tLT4BSQJJSRQrAwNnZ2dkZAJXDw8WAh8BaGRkZLVUsDHz20HvbQGZ1NfcuwtWDajc"""
CONST_EVENTVALIDATION = """/wEWjQECt+HqrA4Cq8PapwoCgqnPlQECypTxxQ4CwPyMgQgC5evuqgIC6KaP6wkC/oLBtwQC4uX5gA8C14+53gcC6Kab6wkC76ab6wkC2OviqgIC/oLFtwQCk7inwQkCtNe56gMCyc6b9wUCzM6b9wUCkbjfwAkC/ILxtwQC7qaT6wkCkbijwQkCz87n9wUCrcXa9wYC6Kaf6wkCr8Wu9AYClrinwQkCwPyEgQgC5evmqgIC6aab6wkCk7jbwAkCtNe96gMCyc6f9wUC6KaT6wkC14+x3gcCr8Wm9AYCwPy4gQgC5euaqgIC/oL9twQCk7jfwAkCtNex6gMCyc6T9wUC14+13gcC6KaX6wkCr8Xa9wYCosWu9AYCx/yAgQgCwPy8gQgCq9e56gMC/oLxtwQCk7jTwAkC4uXpgA8C14+p3gcC6KaL6wkC/oL1twQCk7jXwAkCtNep6gMC14+t3gcCr8Wi9AYCyc6L9wUC14+h3gcC5euWqgIC/oLptwQCrsKviwgCk7jLwAkCtNet6gMCyc6P9wUC4uXhgA8CwPyogQgC/oLttwQCk7jPwAkCtNeh6gMCyc6D9wUC4uXlgA8C14+l3gcC6KaD6wkC5euKqgIC6KaH6wkCr8WK9AYCwPzsgQgCrMWq9AYCk7iDwQkCyc7H9wUCtNfl6gMCo6LFsgkC7N2TuQoC0dnVsgwC6b6sgAgC2M+tigwCgI30tA8CgMb8zgcC9ubt7gcC/+bt7gcChMPv7gcCzPT7pg8Cy5z4SQKE467CAwKOw7XSBAKm8+a5DAL9jpr8BwLl86xxAqqM+voDAsnPktUOAo2+8NQEAsnP7tUOAqLWzMgIAvSgiP4EApOaqosJAr7zxZUPAqXku74FApOa/ogJAsnPotUOAvSg3P8EAqLWgMgIAof95r8CAsDd3cgLAqiXpuEKAo2+hNQEAsDd2cgLAqXkv74FAr7znZUPApOa4ogJAvSgwP8EAof96r8CAqLWhMgIAqiXquEKAo2+iNQEAqXk674FAof90r8CAoGEluMCAs77wOgBAubrvI0OAubr0JMOAtXp0OYFAubrxJMOAty+170NAvSuq9gCAvSux8YCArT3sPAMAsSEhIALAqWf84sCXp+qkQNDhd+vIVvH7GiXwoKmnts="""

college_sgpa_list = []

all_colleges = [
    "17001570001",
    "17003570001",
    "17009570001",
    "17013570001",
    "17015570001",
    "17020570001",
    "17021570001",
    "17025570001",
    "17029570001",
    "17033570001",
    "17035570001",
    "17044570001",
    "17053570001",
    "17058570001",
    "17059570001",
    "17066570001",
    "17067570001",
    "17068570001",
    "17075570001",
    "17078570001"
    ]


for col in all_colleges:
    CONST_college_roll_no = col

    VAR_college_Code = CONST_college_roll_no[2:5]


    r= requests.get('http://duexam2.du.ac.in/RSLT_ND2017/Students/List_Of_Students.aspx?StdType=REG&ExamFlag=CBCS&CourseCode=570&CourseName=(CBCS)%20B.SC.(HONS.)%20COMPUTER%20SCIENCE&Part=I&Sem=I')
    soup = BeautifulSoup(r.text, 'html.parser')
    students_table = soup.find("table", {"rules": "all"})
    data = []
    all_students = students_table.find_all('tr')

    for student in all_students:
        cols = student.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values


    data[0] = ['sno','srollno','sname','sfathername']
    data.pop(0)


    roll_no_pattern = CONST_college_roll_no[:-3] + '...'

    import re
    dduc = []
    for student in data:
        if re.match(roll_no_pattern,student[1]):
            dduc.append(student)
        
    # print(*dduc,sep="\n")


    # for these students make html

    for VAR_stud in dduc:
        VAR_rollno = VAR_stud[1]
        VAR_sname = VAR_stud[2]


        payload = {
            'ddlcollege' : VAR_college_Code,
            'ddlexamtype' : 'Semester',
            'ddlexamflag' : 'CBCS',
            'ddlstream' : 'SC',
            'ddlcourse' : '570',
            'ddlpart' : 'I',
            'ddlsem': 'I',
            'txtrollno' : VAR_rollno,
            'txtname' : VAR_sname,
            'btnsearch': 'Print Score Cart/Transcript',
            '__EVENTTARGET' : '',
            '__EVENTARGUMENT' : '',
            '__LASTFOCUS':'',
            '__VIEWSTATE': CONST_VIEWSTATE,
            '__EVENTVALIDATION': CONST_EVENTVALIDATION
            }

        r = requests.post("http://duexam2.du.ac.in/RSLT_ND2017/Students/Combine_GradeCard.aspx", data=payload)

        #print(r.text)

        soup = BeautifulSoup(r.text, 'html.parser')
        if soup == None:
            continue
        
        for img in soup.find_all('img'):
            img.decompose()

        t = soup.find('span', attrs={'id':'lblstatement'}).decompose()
        t = soup.find('span', attrs={'id':'lbl_sub_head3'}).decompose()
        t = soup.find('span', attrs={'id':'lbldisclaimer'}).decompose()

        sgpa_table = soup.find("table", {"id": "gv_sgpa"})
        if(sgpa_table == None ):
            continue
        sgpa_row = sgpa_table.find_all('td')
        
        temp = []
        for cols in sgpa_row:
            cols = [ele for ele in cols]
            temp.append([ele for ele in cols if ele!=[]]) # Get rid of empty values
        
        college_sgpa_list.append([VAR_rollno, VAR_sname, float(temp[3][0]) ])

        
        '''
        # writing result to html file
        
        VAR_filename = "dduc_marks/" + VAR_rollno + '__' + VAR_sname + '__' + '.html'
        with open(VAR_filename, "w") as file:
            file.write(str(soup))
        '''

college_sgpa_list.sort(key = lambda x : x[2], reverse=True)
#print(college_sgpa_list)


import sys
sys.stdout = open('DU_marks_list.txt', 'w')

print('{3:5} {0:15} {1:25} {2:5}'.format("Roll No.","Name","SGPA","S.No"))
for i,marks in enumerate(college_sgpa_list):
    print('{3:5} {0:15} {1:25} {2:5}'.format(marks[0],marks[1],marks[2], i+1))
