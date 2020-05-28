# Install the Python library from https://pypi.org/project/amadeus
from amadeus import Client, ResponseError

amadeus = Client(
    client_id='YOUR_AMADEUS_API_KEY',
    client_secret='YOUR_AMADEUS_API_SECRET'
)

booking_base64 = 'UmVjZWl2ZWQ6IGZyb20gTVVDRVhNQlhDQVNQMDUuaWlzLmFtYWRldXMubmV0ICgxNzIuMTkuMTMxLjY0KSBieQ0KIE1VQ0VYTUJYQ0FTUDAxLmlpcy5hbWFkZXVzLm5ldCAoMTcyLjE5LjEzMS45KSB3aXRoIE1pY3Jvc29mdCBTTVRQIFNlcnZlcg0KIChUTFMpIGlkIDE1LjAuMTQ5Ny4yIHZpYSBNYWlsYm94IFRyYW5zcG9ydDsgVGh1LCA5IEFwciAyMDIwIDA4OjIyOjM0ICswMDAwDQpSZWNlaXZlZDogZnJvbSBNVUNFWENBU1AwMy5paXMuYW1hZGV1cy5uZXQgKDE3Mi4xOS4xMzEuNzMpIGJ5DQogTVVDRVhNQlhDQVNQMDUuaWlzLmFtYWRldXMubmV0ICgxNzIuMTkuMTMxLjY0KSB3aXRoIE1pY3Jvc29mdCBTTVRQIFNlcnZlcg0KIChUTFMpIGlkIDE1LjAuMTQ5Ny4yOyBUaHUsIDkgQXByIDIwMjAgMDg6MjI6MzQgKzAwMDANClJlY2VpdmVkOiBmcm9tIE1VQ0VYRURHRVAwNC5paXMuYW1hZGV1cy5uZXQgKDE3Mi4xOS4xMzQuMzIpIGJ5DQogTVVDRVhDQVNQMDMuaWlzLmFtYWRldXMubmV0ICgxNzIuMTkuMTMxLjczKSB3aXRoIE1pY3Jvc29mdCBTTVRQIFNlcnZlciAoVExTKQ0KIGlkIDE1LjAuMTQ5Ny4yOyBUaHUsIDkgQXByIDIwMjAgMDg6MjI6MzMgKzAwMDANClJlY2VpdmVkOiBmcm9tIEVVUjAyLUFNNS1vYmUub3V0Ym91bmQucHJvdGVjdGlvbi5vdXRsb29rLmNvbSAoMTA0LjQ3LjQuNTkpIGJ5DQogc210cGV4Y2guYW1hZGV1cy5jb20gKDE3Mi4xOS4xMzQuMzIpIHdpdGggTWljcm9zb2Z0IFNNVFAgU2VydmVyIChUTFMpIGlkDQogMTUuMC4xNDk3LjI7IFRodSwgOSBBcHIgMjAyMCAwODoyMjozMiArMDAwMA0KUmVjZWl2ZWQ6IGZyb20gQU0wUFIxME1CMjE5My5FVVJQUkQxMC5QUk9ELk9VVExPT0suQ09NICgyMC4xNzcuMTA4LjE0NikgYnkNCiBBTTBQUjEwTUIzNjE4LkVVUlBSRDEwLlBST0QuT1VUTE9PSy5DT00gKDEwLjE4Ni4xNzIuMTQzKSB3aXRoIE1pY3Jvc29mdCBTTVRQDQogU2VydmVyICh2ZXJzaW9uPVRMUzFfMiwgY2lwaGVyPVRMU19FQ0RIRV9SU0FfV0lUSF9BRVNfMjU2X0dDTV9TSEEzODQpIGlkDQogMTUuMjAuMjg3OC4xNjsgVGh1LCA5IEFwciAyMDIwIDA4OjIyOjMxICswMDAwDQpSZWNlaXZlZDogZnJvbSBBTTBQUjEwTUIyMTkzLkVVUlBSRDEwLlBST0QuT1VUTE9PSy5DT00NCiAoW2ZlODA6OjY0ZmU6NGFmYjpmMzUwOmZmZTRdKSBieSBBTTBQUjEwTUIyMTkzLkVVUlBSRDEwLlBST0QuT1VUTE9PSy5DT00NCiAoW2ZlODA6OjY0ZmU6NGFmYjpmMzUwOmZmZTQlN10pIHdpdGggbWFwaSBpZCAxNS4yMC4yODc4LjAyMTsgVGh1LCA5IEFwciAyMDIwDQogMDg6MjI6MzEgKzAwMDANCkZyb206IE1lZ2hhbmEgRCA8bWVnaGFuYS5kQGFtYWRldXMuY29tPg0KVG86IFpaLUJMUi1hbWFtb2JpbGVwYXJzaW5nLWRldjEgPFpaLUJMUi1hbWFtb2JpbGVwYXJzaW5nLWRldjFAYW1hZGV1cy5jb20+DQpTdWJqZWN0OiBGVzogVVBBREhZQVlFL1BBUklESEkgTVMgMjBBUFIgTEhSIENERw0KVGhyZWFkLVRvcGljOiBVUEFESFlBWUUvUEFSSURISSBNUyAyMEFQUiBMSFIgQ0RHDQpUaHJlYWQtSW5kZXg6IEFRSFdEajBIWFE0SllRY1A0RUMwWjhUNXE5cE9rYWh3YklQUWdBQURFYUNBQUFQbGNBPT0NCkRhdGU6IFRodSwgOSBBcHIgMjAyMCAwODoyMjozMSArMDAwMA0KTWVzc2FnZS1JRDoNCgk8QU0wUFIxME1CMjE5M0M5QjY0QjUwQzgxNzEzN0YzNDUxRkNDMTBAQU0wUFIxME1CMjE5My5FVVJQUkQxMC5QUk9ELk9VVExPT0suQ09NPg0KUmVmZXJlbmNlczogPENUUy9CQS9DNTBFMTMxNjQyMEMvMUB0ZHMuYW1hZGV1cy5jb20+DQogPEFNN1BSMTBNQjM4ODlFOTcwOEIwMUZDOTYwNURBNzJEQjk3QzEwQEFNN1BSMTBNQjM4ODkuRVVSUFJEMTAuUFJPRC5PVVRMT09LLkNPTT4NCiA8QU0wUFIxME1CMjE5M0UxNDk2Qzc3MzBFODkyNjcxNkQwRkNDMTBAQU0wUFIxME1CMjE5My5FVVJQUkQxMC5QUk9ELk9VVExPT0suQ09NPg0KSW4tUmVwbHktVG86DQoJPEFNMFBSMTBNQjIxOTNFMTQ5NkM3NzMwRTg5MjY3MTZEMEZDQzEwQEFNMFBSMTBNQjIxOTMuRVVSUFJEMTAuUFJPRC5PVVRMT09LLkNPTT4NCkFjY2VwdC1MYW5ndWFnZTogZW4tVVMNCkNvbnRlbnQtTGFuZ3VhZ2U6IGVuLVVTDQpYLU1TLUV4Y2hhbmdlLU9yZ2FuaXphdGlvbi1BdXRoQXM6IEludGVybmFsDQpYLU1TLUV4Y2hhbmdlLU9yZ2FuaXphdGlvbi1BdXRoTWVjaGFuaXNtOiAwNA0KWC1NUy1FeGNoYW5nZS1Pcmdhbml6YXRpb24tQXV0aFNvdXJjZTogQU0wUFIxME1CMjE5My5FVVJQUkQxMC5QUk9ELk9VVExPT0suQ09NDQpYLU1TLUhhcy1BdHRhY2g6DQpYLU1TLUV4Y2hhbmdlLU9yZ2FuaXphdGlvbi1TQ0w6IC0xDQpYLU1TLVRORUYtQ29ycmVsYXRvcjoNCkNvbnRlbnQtVHlwZTogbXVsdGlwYXJ0L2FsdGVybmF0aXZlOw0KCWJvdW5kYXJ5PSJfMDAwX0FNMFBSMTBNQjIxOTNDOUI2NEI1MEM4MTcxMzdGMzQ1MUZDQzEwQU0wUFIxME1CMjE5M0VVUlBfIg0KTUlNRS1WZXJzaW9uOiAxLjANCg0KLS1fMDAwX0FNMFBSMTBNQjIxOTNDOUI2NEI1MEM4MTcxMzdGMzQ1MUZDQzEwQU0wUFIxME1CMjE5M0VVUlBfDQpDb250ZW50LVR5cGU6IHRleHQvcGxhaW47IGNoYXJzZXQ9InVzLWFzY2lpIg0KDQpDT05GSURFTlRJQUwgJiBSRVNUUklDVEVEDQoNCg0KDQpGcm9tOiBNZWdoYW5hIEQNClNlbnQ6IFRodXJzZGF5LCBBcHJpbCA5LCAyMDIwIDE6NDIgUE0NClRvOiBaWi1CTFItVENNLURFVjEgPGJsci50Y20uZGV2MUBhbWFkZXVzLmNvbT4NClN1YmplY3Q6IEZXOiBVUEFESFlBWUUvUEFSSURISSBNUyAyMEFQUiBMSFIgQ0RHDQoNCg0KQ09ORklERU5USUFMICYgUkVTVFJJQ1RFRA0KDQoNCg0KRnJvbTogUGFyaWRoaSBVUEFESFlBWQ0KU2VudDogVGh1cnNkYXksIEFwcmlsIDksIDIwMjAgMToyNyBQTQ0KVG86IE1lZ2hhbmEgRCA8bWVnaGFuYS5kQGFtYWRldXMuY29tPG1haWx0bzptZWdoYW5hLmRAYW1hZGV1cy5jb20+Pg0KU3ViamVjdDogRlc6IFVQQURIWUFZRS9QQVJJREhJIE1TIDIwQVBSIExIUiBDREcNCg0KDQpDT05GSURFTlRJQUwgJiBSRVNUUklDVEVEDQoNCg0KDQpGcm9tOiAiQnJpdGlzaCBBaXJ3YXlzIFBsYyAoQmFzcykgIiA8ZXRpY2tldEBhbWFkZXVzLmNvbTxtYWlsdG86ZXRpY2tldEBhbWFkZXVzLmNvbT4+DQpTZW50OiBUaHVyc2RheSwgQXByaWwgOSwgMjAyMCAxMjozNCBQTQ0KVG86IFBhcmlkaGkgVVBBREhZQVkgPFBhcmlkaGkuVVBBREhZQVlAYW1hZGV1cy5jb208bWFpbHRvOlBhcmlkaGkuVVBBREhZQVlAYW1hZGV1cy5jb20+Pg0KU3ViamVjdDogVVBBREhZQVlFL1BBUklESEkgTVMgMjBBUFIgTEhSIENERw0KDQpDQVVUSU9OOiBUaGlzIGVtYWlsIG9yaWdpbmF0ZWQgZnJvbSBvdXRzaWRlIG9mIHRoZSBvcmdhbml6YXRpb24uIERvIG5vdCBjbGljayBsaW5rcyBvciBvcGVuIGF0dGFjaG1lbnRzIHVubGVzcyB5b3UgcmVjb2duaXplIHRoZSBzZW5kZXIgYW5kIGtub3cgdGhlIGNvbnRlbnQgaXMgc2FmZS4NCg0KDQpVUEFESFlBWUUvUEFSSURISSBNUyAyMEFQUiBMSFIgQ0RHDQoNCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQ0KDQoNCg0KVGhpcyBkb2N1bWVudCBpcyBhdXRvbWF0aWNhbGx5IGdlbmVyYXRlZC4NCg0KUGxlYXNlIGRvIG5vdCByZXNwb25kIHRvIHRoaXMgbWFpbC4NCg0KDQoNCg0KDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgRUxFQ1RST05JQyBUSUNLRVQNCg0KICAgICAgICAgICAgICAgICAgICAgICBQQVNTRU5HRVIgSVRJTkVSQVJZIFJFQ0VJUFQNCg0KDQoNCiBCUklUSVNIIEFJUldBWVMgUExDIChCQVNTKSAgICAgICAgIERBVEU6IDA5IEFQUiAyMDIwDQoNCiBSRVZFTlVFIE1BTkFHRU1FTlQuIFNFTExJTkcgICAgICAgQUdFTlQ6IDgwMTkNCg0KIFNZU1RFTVMuDQoNCiBBVVNUUkFMQVNJQSBIQkEyICAgICAgICAgICAgICAgICAgIE5BTUU6IFVQQURIWUFZRS9QQVJJREhJIE1TDQoNCiBMT05ET04NCg0KIElBVEEgICAgICAgOiA5MTQgMDM5MTENCg0KIFRFTEVQSE9ORSAgOiAwODQ1IDQ5MyAwIDc4Nw0KDQoNCg0KIElTU1VJTkcgQUlSTElORSAgICAgICAgICAgICAgICAgICAgICAgIDogQlJJVElTSCBBSVJXQVlTDQoNCiBUSUNLRVQgTlVNQkVSICAgICAgICAgICAgICAgICAgICAgICAgICA6IEVUS1QgMTI1IDIxMDYyNzQ4MDYNCg0KIEJPT0tJTkcgUkVGIDogQU1BREVVUzogTzNWTVBTLCBBSVJMSU5FOiBCQS9PM1ZNUFMNCg0KDQoNCiBGUk9NIC9UTyAgICAgICAgRkxJR0hUICBDTCBEQVRFICAgREVQICAgICAgRkFSRSBCQVNJUyAgICBOVkIgICBOVkEgICBCQUcgIFNUDQoNCg0KDQogTE9ORE9OIEhFQVRIUk9XIEJBIDMwNCAgViAgMjBBUFIgIDA3MjAgICAgIFZaMFJPICAgICAgICAgMjBBUFIgMjBBUFIgMFBDICBPSw0KDQogVEVSTUlOQUw6NQ0KDQogUEFSSVMgQ0hBUkxFUyAgICAgICAgICAgICAgICAgICAgQVJSSVZBTCBUSU1FOiAwOTM1ICAgQVJSSVZBTCBEQVRFOiAyMEFQUg0KDQogREUgR0FVTExFDQoNCiBURVJNSU5BTDoyQQ0KDQogQk9BUkRJTkcgVElNRTogMjAgQVBSSUwgMDY6NTAgKFNVQkpFQ1QgVE8gQ0hBTkdFKQ0KDQoNCg0KDQoNCiBBVCBDSEVDSy1JTiwgUExFQVNFIFNIT1cgQSBQSUNUVVJFIElERU5USUZJQ0FUSU9OIEFORCBUSEUgRE9DVU1FTlQgWU9VIEdBVkUNCg0KIEZPUiBSRUZFUkVOQ0UgQVQgUkVTRVJWQVRJT04gVElNRQ0KDQoNCg0KIENBUlJZLU9OIEJBRzoNCg0KIFBMRUFTRSBDT05UQUNUIFlPVVIgQUdFTlQuDQoNCg0KDQoNCg0KIEJBR0dBR0UgUFJPSElCSVRFRDogTk9UIEFQUExJQ0FCTEUNCg0KIEVORE9SU0VNRU5UUyAgOiBOT05SRUYvSEJPIC1aMFINCg0KIFBBWU1FTlQgICAgICAgOiBDQQ0KDQoNCg0KIEZBUkUgQ0FMQ1VMQVRJT04gICA6TE9OIEJBIFBBUjEyOC4wNE5VQzEyOC4wNEVORCBST0UwLjc3MzE1MA0KDQoNCg0KIEFJUiBGQVJFICAgICAgICAgICA6IEdCUCAgICAgOTkuMDANCg0KIFRBWCAgICAgICAgICAgICAgICA6IEdCUCAgICAgMTMuMDBHQiAgIEdCUCAgICAgMjAuNjRVQg0KDQogVE9UQUwgICAgICAgICAgICAgIDogR0JQICAgICAxMzIuNjQNCg0KDQoNCg0KDQpJTiBBQ0NPUkRBTkNFIFdJVEggVEhFIEdSRU5FTExFIExBVyBZT1UgQ0FOIERJU1BMQVkgVEhFIElORk9STUFUSU9OIFJFTEFURUQgVE8NCg0KVEhFIENBUkJPTiBDT05TVU1FRCA6IENMSUNLIEhFUkUNCg0KaHR0cHM6Ly9jbGlja3RpbWUuc3ltYW50ZWMuY29tLzNZWXVRNnI3MUs0bWRRcnJtdkwySkEzNkgyP3U9SFRUUCUzQSUyRiUyRldXVy5JQ0FPLklOVCUyRkVOVklST05NRU5UQUwtUFJPVEVDVElPTiUyRkNBUkJPTk9GRlNFVCUyRlBBR0VTJTJGREVGQVVMVC5BU1BYDQoNCg0KDQpOT1RJQ0UNCg0KQ0FSUklBR0UgQU5EIE9USEVSIFNFUlZJQ0VTIFBST1ZJREVEIEJZIFRIRSBDQVJSSUVSIEFSRSBTVUJKRUNUIFRPIENPTkRJVElPTlMNCg0KT0YgQ0FSUklBR0UsIFdISUNIIEFSRSBIRVJFQlkgSU5DT1JQT1JBVEVEIEJZIFJFRkVSRU5DRS4gVEhFU0UgQ09ORElUSU9OUyBNQVkNCg0KQkUgT0JUQUlORUQgRlJPTSBUSEUgSVNTVUlORyBDQVJSSUVSLg0KDQoNCg0KVEhFIEJSSVRJU0ggQUlSV0FZUyBGUkVFIENIRUNLRUQgQkFHR0FHRSBBTExPV0FOQ0UgSU5DTFVERVMgQkFHUyBVUCBUTw0KDQoyM0tHUy81MUxCUyBBTkQvT1IgU1BPUlRJTkcgRVFVSVBNRU5ULCBNVVNJQ0FMIElOU1RSVU1FTlRTLCBGSUxNDQoNCkVRVUlQTUVOVCBBTEwgTUVBU1VSSU5HIDkwIFggNzUgWCA0M0NNIC8gMzUuNSBYIDI5LjUgWCAxNklOUy4gQkFHUyBPUg0KDQpJVEVNUyBUSEFUIEFSRSBJTiBFWENFU1MgT0YgVEhFIEZSRUUgQUxMT1dBTkNFIEFORC9PUiBFWENFRUQgMjNLRy81MUxCDQoNCk1BWSBCRSBTVUJKRUNUIFRPIEVYQ0VTUyBBTkQvT1IgT1ZFUldFSUdIVCBDSEFSR0VTIEFUIENIRUNLLUlOLg0KDQoNCg0KQ0FCSU4gQkFHR0FHRSBESU1FTlNJT05TIE1VU1QgTk9UIEVYQ0VFRCA1NkNNIFg0NUNNIFggMjVDTSAvIDIySU5TIFgNCg0KMThJTlMgWCAxMElOUyBMQVBUT1AgT1IgSEFOREJBRyBJVEVNUyBNVVNUIE5PVCBFWENFRUQgNDBDTSBYIDMwQ00gWA0KDQoxNUNNLzE2SU5TIFggMTJJTlMgWCA2SU5TLg0KDQpWSVNJVCBodHRwczovL2NsaWNrdGltZS5zeW1hbnRlYy5jb20vM0ZxdlA0UllLYXBXQ2IxNkpOanljN3E2SDI/dT1IVFRQJTNBJTJGJTJGV1dXLkJSSVRJU0hBSVJXQVlTLkNPTSBBTkQgU0VBUkNIIEZPUiBCQUdHQUdFIEZPUiBNT1JFDQoNCkRFVEFJTFMuDQoNCg0KDQpUSEUgSVRJTkVSQVJZL1JFQ0VJUFQgQ09OU1RJVFVURVMgVEhFIFBBU1NFTkdFUiBUSUNLRVQgRk9SIFRIRSBQVVJQT1NFUyBPRg0KDQpBUlRJQ0xFIDMgT0YgVEhFIFdBUlNBVyBDT05WRU5USU9OLCBFWENFUFQgV0hFUkUgVEhFIENBUlJJRVIgREVMSVZFUlMgVE8gVEhFDQoNClBBU1NFTkdFUiBBTk9USEVSIERPQ1VNRU5UIENPTVBMWUlORyBXSVRIIFRIRSBSRVFVSVJFTUVOVFMgT0YgQVJUSUNMRSAzLg0KDQoNCg0KUEFTU0VOR0VSUyBPTiBBIEpPVVJORVkgSU5WT0xWSU5HIEFOIFVMVElNQVRFIERFU1RJTkFUSU9OIE9SIEEgU1RPUCBJTiBBDQoNCkNPVU5UUlkgT1RIRVIgVEhBTiBUSEUgQ09VTlRSWSBPRiBERVBBUlRVUkUgQVJFIEFEVklTRUQgVEhBVCBJTlRFUk5BVElPTkFMDQoNClRSRUFUSUVTIEtOT1dOIEFTIFRIRSBNT05UUkVBTCBDT05WRU5USU9OLCBPUiBJVFMgUFJFREVDRVNTT1IsIFRIRSBXQVJTQVcNCg0KQ09OVkVOVElPTiwgSU5DTFVESU5HIElUUyBBTUVORE1FTlRTIChUSEUgV0FSU0FXIENPTlZFTlRJT04gU1lTVEVNKSwgTUFZIEFQUExZDQoNClRPIFRIRSBFTlRJUkUgSk9VUk5FWSwgSU5DTFVESU5HIEFOWSBQT1JUSU9OIFRIRVJFT0YgV0lUSElOIEEgQ09VTlRSWS4gIEZPUg0KDQpTVUNIIFBBU1NFTkdFUlMsIFRIRSBBUFBMSUNBQkxFIFRSRUFUWSwgSU5DTFVESU5HIFNQRUNJQUwgQ09OVFJBQ1RTIE9GDQoNCkNBUlJJQUdFIEVNQk9ESUVEIElOIEFOWSBBUFBMSUNBQkxFIFRBUklGRlMsIEdPVkVSTlMgQU5EIE1BWSBMSU1JVCBUSEUNCg0KTElBQklMSVRZIE9GIFRIRSBDQVJSSUVSLiBUSEVTRSBDT05WRU5USU9OUyBHT1ZFUk4gQU5EIE1BWSBMSU1JVCBUSEUNCg0KTElBQklMSVRZT0YgQUlSIENBUlJJRVJTIEZPUiBERUFUSCBPUiBCT0RJTFkgSU5KVVJZIE9SIExPU1MgT0YgT1IgREFNQUdFIFRPDQoNCkJBR0dBR0UsIEFORCBGT1IgREVMQVkuDQoNCg0KDQpUSEUgQ0FSUklBR0UgT0YgQ0VSVEFJTiBIQVpBUkRPVVMgTUFURVJJQUxTLCBMSUtFIEFFUk9TT0xTLCBGSVJFV09SS1MsIEFORA0KDQpGTEFNTUFCTEUgTElRVUlEUywgQUJPQVJEIFRIRSBBSVJDUkFGVCBJUyBGT1JCSURERU4uIElGIFlPVSBETyBOT1QgVU5ERVJTVEFORA0KDQpUSEVTRSBSRVNUUklDVElPTlMsIEZVUlRIRVIgSU5GT1JNQVRJT04gTUFZIEJFIE9CVEFJTkVEIEZST00gWU9VUiBBSVJMSU5FLg0KDQoNCg0KREFUQSBQUk9URUNUSU9OIE5PVElDRTogWU9VUiBQRVJTT05BTCBEQVRBIFdJTEwgQkUgUFJPQ0VTU0VEIElOIEFDQ09SREFOQ0UNCg0KV0lUSCBUSEUgQVBQTElDQUJMRSBDQVJSSUVSJ1MgUFJJVkFDWSBQT0xJQ1kgQU5ELCBJRiBZT1VSIEJPT0tJTkcgSVMgTUFERSBWSUENCg0KQSBSRVNFUlZBVElPTiBTWVNURU0gUFJPVklERVIgKCBHRFMgKSwgV0lUSCBJVFMgUFJJVkFDWSBQT0xJQ1kuIFRIRVNFIEFSRQ0KDQpBVkFJTEFCTEUgQVQgaHR0cHM6Ly9jbGlja3RpbWUuc3ltYW50ZWMuY29tLzM1MTh4ZU5yenpTaU1iSzlvQ05qRTZiNkgyP3U9aHR0cCUzQSUyRiUyRnd3dy5pYXRhdHJhdmVsY2VudGVyLmNvbSUyRnByaXZhY3kgT1IgRlJPTSBUSEUgQ0FSUklFUiBPUg0KDQpHRFMgRElSRUNUTFkuIFlPVSBTSE9VTEQgUkVBRCBUSElTIERPQ1VNRU5UQVRJT04sIFdISUNIIEFQUExJRVMgVE8gWU9VUg0KDQpCT09LSU5HIEFORCBTUEVDSUZJRVMsIEZPUiBFWEFNUExFLCBIT1cgWU9VUiBQRVJTT05BTCBEQVRBIElTIENPTExFQ1RFRCwNCg0KU1RPUkVELCBVU0VELCBESVNDTE9TRUQgQU5EIFRSQU5TRkVSUkVELihBUFBMSUNBQkxFIEZPUiBJTlRFUkxJTkUgQ0FSUklBR0UpDQoNCi0tXzAwMF9BTTBQUjEwTUIyMTkzQzlCNjRCNTBDODE3MTM3RjM0NTFGQ0MxMEFNMFBSMTBNQjIxOTNFVVJQXw0KQ29udGVudC1UeXBlOiB0ZXh0L2h0bWw7IGNoYXJzZXQ9InVzLWFzY2lpIg0KDQo8aHRtbCB4bWxuczp2PSJ1cm46c2NoZW1hcy1taWNyb3NvZnQtY29tOnZtbCIgeG1sbnM6bz0idXJuOnNjaGVtYXMtbWljcm9zb2Z0LWNvbTpvZmZpY2U6b2ZmaWNlIiB4bWxuczp3PSJ1cm46c2NoZW1hcy1taWNyb3NvZnQtY29tOm9mZmljZTp3b3JkIiB4bWxuczptPSJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL29mZmljZS8yMDA0LzEyL29tbWwiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy9UUi9SRUMtaHRtbDQwIj4NCjxoZWFkPg0KPG1ldGEgaHR0cC1lcXVpdj0iQ29udGVudC1UeXBlIiBjb250ZW50PSJ0ZXh0L2h0bWw7IGNoYXJzZXQ9dXMtYXNjaWkiPg0KPG1ldGEgbmFtZT0iR2VuZXJhdG9yIiBjb250ZW50PSJNaWNyb3NvZnQgV29yZCAxNSAoZmlsdGVyZWQgbWVkaXVtKSI+DQo8c3R5bGU+PCEtLQ0KLyogRm9udCBEZWZpbml0aW9ucyAqLw0KQGZvbnQtZmFjZQ0KCXtmb250LWZhbWlseToiQ2FtYnJpYSBNYXRoIjsNCglwYW5vc2UtMToyIDQgNSAzIDUgNCA2IDMgMiA0O30NCkBmb250LWZhY2UNCgl7Zm9udC1mYW1pbHk6Q2FsaWJyaTsNCglwYW5vc2UtMToyIDE1IDUgMiAyIDIgNCAzIDIgNDt9DQpAZm9udC1mYWNlDQoJe2ZvbnQtZmFtaWx5OkNvbnNvbGFzOw0KCXBhbm9zZS0xOjIgMTEgNiA5IDIgMiA0IDMgMiA0O30NCi8qIFN0eWxlIERlZmluaXRpb25zICovDQpwLk1zb05vcm1hbCwgbGkuTXNvTm9ybWFsLCBkaXYuTXNvTm9ybWFsDQoJe21hcmdpbjowaW47DQoJbWFyZ2luLWJvdHRvbTouMDAwMXB0Ow0KCWZvbnQtc2l6ZToxMS4wcHQ7DQoJZm9udC1mYW1pbHk6IkNhbGlicmkiLHNhbnMtc2VyaWY7fQ0KYTpsaW5rLCBzcGFuLk1zb0h5cGVybGluaw0KCXttc28tc3R5bGUtcHJpb3JpdHk6OTk7DQoJY29sb3I6IzA1NjNDMTsNCgl0ZXh0LWRlY29yYXRpb246dW5kZXJsaW5lO30NCmE6dmlzaXRlZCwgc3Bhbi5Nc29IeXBlcmxpbmtGb2xsb3dlZA0KCXttc28tc3R5bGUtcHJpb3JpdHk6OTk7DQoJY29sb3I6Izk1NEY3MjsNCgl0ZXh0LWRlY29yYXRpb246dW5kZXJsaW5lO30NCnByZQ0KCXttc28tc3R5bGUtcHJpb3JpdHk6OTk7DQoJbXNvLXN0eWxlLWxpbms6IkhUTUwgUHJlZm9ybWF0dGVkIENoYXIiOw0KCW1hcmdpbjowaW47DQoJbWFyZ2luLWJvdHRvbTouMDAwMXB0Ow0KCWZvbnQtc2l6ZToxMC4wcHQ7DQoJZm9udC1mYW1pbHk6IkNvdXJpZXIgTmV3Ijt9DQpzcGFuLkhUTUxQcmVmb3JtYXR0ZWRDaGFyDQoJe21zby1zdHlsZS1uYW1lOiJIVE1MIFByZWZvcm1hdHRlZCBDaGFyIjsNCgltc28tc3R5bGUtcHJpb3JpdHk6OTk7DQoJbXNvLXN0eWxlLWxpbms6IkhUTUwgUHJlZm9ybWF0dGVkIjsNCglmb250LWZhbWlseTpDb25zb2xhczt9DQpwLm1zb25vcm1hbDAsIGxpLm1zb25vcm1hbDAsIGRpdi5tc29ub3JtYWwwDQoJe21zby1zdHlsZS1uYW1lOm1zb25vcm1hbDsNCgltc28tbWFyZ2luLXRvcC1hbHQ6YXV0bzsNCgltYXJnaW4tcmlnaHQ6MGluOw0KCW1zby1tYXJnaW4tYm90dG9tLWFsdDphdXRvOw0KCW1hcmdpbi1sZWZ0OjBpbjsNCglmb250LXNpemU6MTEuMHB0Ow0KCWZvbnQtZmFtaWx5OiJDYWxpYnJpIixzYW5zLXNlcmlmO30NCnAubXNpcGhlYWRlcmM1OGY1YjIxLCBsaS5tc2lwaGVhZGVyYzU4ZjViMjEsIGRpdi5tc2lwaGVhZGVyYzU4ZjViMjENCgl7bXNvLXN0eWxlLW5hbWU6bXNpcGhlYWRlcmM1OGY1YjIxOw0KCW1zby1tYXJnaW4tdG9wLWFsdDphdXRvOw0KCW1hcmdpbi1yaWdodDowaW47DQoJbXNvLW1hcmdpbi1ib3R0b20tYWx0OmF1dG87DQoJbWFyZ2luLWxlZnQ6MGluOw0KCWZvbnQtc2l6ZToxMS4wcHQ7DQoJZm9udC1mYW1pbHk6IkNhbGlicmkiLHNhbnMtc2VyaWY7fQ0Kc3Bhbi5FbWFpbFN0eWxlMjENCgl7bXNvLXN0eWxlLXR5cGU6cGVyc29uYWw7DQoJZm9udC1mYW1pbHk6IkNhbGlicmkiLHNhbnMtc2VyaWY7DQoJY29sb3I6d2luZG93dGV4dDt9DQpzcGFuLkVtYWlsU3R5bGUyMg0KCXttc28tc3R5bGUtdHlwZTpwZXJzb25hbDsNCglmb250LWZhbWlseToiQ2FsaWJyaSIsc2Fucy1zZXJpZjsNCgljb2xvcjp3aW5kb3d0ZXh0O30NCnNwYW4uRW1haWxTdHlsZTIzDQoJe21zby1zdHlsZS10eXBlOnBlcnNvbmFsLXJlcGx5Ow0KCWZvbnQtZmFtaWx5OiJDYWxpYnJpIixzYW5zLXNlcmlmOw0KCWNvbG9yOndpbmRvd3RleHQ7fQ0KLk1zb0NocERlZmF1bHQNCgl7bXNvLXN0eWxlLXR5cGU6ZXhwb3J0LW9ubHk7DQoJZm9udC1zaXplOjEwLjBwdDt9DQpAcGFnZSBXb3JkU2VjdGlvbjENCgl7c2l6ZTo4LjVpbiAxMS4waW47DQoJbWFyZ2luOjEuMGluIDEuMGluIDEuMGluIDEuMGluO30NCmRpdi5Xb3JkU2VjdGlvbjENCgl7cGFnZTpXb3JkU2VjdGlvbjE7fQ0KLS0+PC9zdHlsZT48IS0tW2lmIGd0ZSBtc28gOV0+PHhtbD4NCjxvOnNoYXBlZGVmYXVsdHMgdjpleHQ9ImVkaXQiIHNwaWRtYXg9IjEwMjYiIC8+DQo8L3htbD48IVtlbmRpZl0tLT48IS0tW2lmIGd0ZSBtc28gOV0+PHhtbD4NCjxvOnNoYXBlbGF5b3V0IHY6ZXh0PSJlZGl0Ij4NCjxvOmlkbWFwIHY6ZXh0PSJlZGl0IiBkYXRhPSIxIiAvPg0KPC9vOnNoYXBlbGF5b3V0PjwveG1sPjwhW2VuZGlmXS0tPg0KPC9oZWFkPg0KPGJvZHkgbGFuZz0iRU4tVVMiIGxpbms9IiMwNTYzQzEiIHZsaW5rPSIjOTU0RjcyIj4NCjxkaXYgY2xhc3M9IldvcmRTZWN0aW9uMSI+DQo8cCBjbGFzcz0ibXNpcGhlYWRlcmM1OGY1YjIxIiBhbGlnbj0icmlnaHQiIHN0eWxlPSJtYXJnaW46MGluO21hcmdpbi1ib3R0b206LjAwMDFwdDt0ZXh0LWFsaWduOnJpZ2h0Ij4NCjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTIuMHB0O2NvbG9yOmRhcmtvcmFuZ2UiPkNPTkZJREVOVElBTCAmYW1wOyBSRVNUUklDVEVEPC9zcGFuPjxvOnA+PC9vOnA+PC9wPg0KPHAgY2xhc3M9Ik1zb05vcm1hbCI+PG86cD4mbmJzcDs8L286cD48L3A+DQo8cCBjbGFzcz0iTXNvTm9ybWFsIj48bzpwPiZuYnNwOzwvbzpwPjwvcD4NCjxwIGNsYXNzPSJNc29Ob3JtYWwiPjxvOnA+Jm5ic3A7PC9vOnA+PC9wPg0KPGRpdj4NCjxkaXYgc3R5bGU9ImJvcmRlcjpub25lO2JvcmRlci10b3A6c29saWQgI0UxRTFFMSAxLjBwdDtwYWRkaW5nOjMuMHB0IDBpbiAwaW4gMGluIj4NCjxwIGNsYXNzPSJNc29Ob3JtYWwiPjxiPkZyb206PC9iPiBNZWdoYW5hIEQgPGJyPg0KPGI+U2VudDo8L2I+IFRodXJzZGF5LCBBcHJpbCA5LCAyMDIwIDE6NDIgUE08YnI+DQo8Yj5Ubzo8L2I+IFpaLUJMUi1UQ00tREVWMSAmbHQ7YmxyLnRjbS5kZXYxQGFtYWRldXMuY29tJmd0Ozxicj4NCjxiPlN1YmplY3Q6PC9iPiBGVzogVVBBREhZQVlFL1BBUklESEkgTVMgMjBBUFIgTEhSIENERzxvOnA+PC9vOnA+PC9wPg0KPC9kaXY+DQo8L2Rpdj4NCjxwIGNsYXNzPSJNc29Ob3JtYWwiPjxvOnA+Jm5ic3A7PC9vOnA+PC9wPg0KPHAgY2xhc3M9Im1zaXBoZWFkZXJjNThmNWIyMSIgYWxpZ249InJpZ2h0IiBzdHlsZT0ibWFyZ2luOjBpbjttYXJnaW4tYm90dG9tOi4wMDAxcHQ7dGV4dC1hbGlnbjpyaWdodCI+DQo8c3BhbiBzdHlsZT0iZm9udC1zaXplOjEyLjBwdDtjb2xvcjpkYXJrb3JhbmdlIj5DT05GSURFTlRJQUwgJmFtcDsgUkVTVFJJQ1RFRDwvc3Bhbj48bzpwPjwvbzpwPjwvcD4NCjxwIGNsYXNzPSJNc29Ob3JtYWwiPjxvOnA+Jm5ic3A7PC9vOnA+PC9wPg0KPHAgY2xhc3M9Ik1zb05vcm1hbCI+PG86cD4mbmJzcDs8L286cD48L3A+DQo8cCBjbGFzcz0iTXNvTm9ybWFsIj48bzpwPiZuYnNwOzwvbzpwPjwvcD4NCjxkaXY+DQo8ZGl2IHN0eWxlPSJib3JkZXI6bm9uZTtib3JkZXItdG9wOnNvbGlkICNFMUUxRTEgMS4wcHQ7cGFkZGluZzozLjBwdCAwaW4gMGluIDBpbiI+DQo8cCBjbGFzcz0iTXNvTm9ybWFsIj48Yj5Gcm9tOjwvYj4gUGFyaWRoaSBVUEFESFlBWSA8YnI+DQo8Yj5TZW50OjwvYj4gVGh1cnNkYXksIEFwcmlsIDksIDIwMjAgMToyNyBQTTxicj4NCjxiPlRvOjwvYj4gTWVnaGFuYSBEICZsdDs8YSBocmVmPSJtYWlsdG86bWVnaGFuYS5kQGFtYWRldXMuY29tIj5tZWdoYW5hLmRAYW1hZGV1cy5jb208L2E+Jmd0Ozxicj4NCjxiPlN1YmplY3Q6PC9iPiBGVzogVVBBREhZQVlFL1BBUklESEkgTVMgMjBBUFIgTEhSIENERzxvOnA+PC9vOnA+PC9wPg0KPC9kaXY+DQo8L2Rpdj4NCjxwIGNsYXNzPSJNc29Ob3JtYWwiPjxvOnA+Jm5ic3A7PC9vOnA+PC9wPg0KPHAgY2xhc3M9Im1zaXBoZWFkZXJjNThmNWIyMSIgYWxpZ249InJpZ2h0IiBzdHlsZT0ibWFyZ2luOjBpbjttYXJnaW4tYm90dG9tOi4wMDAxcHQ7dGV4dC1hbGlnbjpyaWdodCI+DQo8c3BhbiBzdHlsZT0iZm9udC1zaXplOjEyLjBwdDtjb2xvcjpkYXJrb3JhbmdlIj5DT05GSURFTlRJQUwgJmFtcDsgUkVTVFJJQ1RFRDwvc3Bhbj48bzpwPjwvbzpwPjwvcD4NCjxwIGNsYXNzPSJNc29Ob3JtYWwiPjxvOnA+Jm5ic3A7PC9vOnA+PC9wPg0KPHAgY2xhc3M9Ik1zb05vcm1hbCI+PG86cD4mbmJzcDs8L286cD48L3A+DQo8cCBjbGFzcz0iTXNvTm9ybWFsIj48bzpwPiZuYnNwOzwvbzpwPjwvcD4NCjxkaXY+DQo8ZGl2IHN0eWxlPSJib3JkZXI6bm9uZTtib3JkZXItdG9wOnNvbGlkICNFMUUxRTEgMS4wcHQ7cGFkZGluZzozLjBwdCAwaW4gMGluIDBpbiI+DQo8cCBjbGFzcz0iTXNvTm9ybWFsIj48Yj5Gcm9tOjwvYj4gJnF1b3Q7QnJpdGlzaCBBaXJ3YXlzIFBsYyAoQmFzcykgJnF1b3Q7ICZsdDs8YSBocmVmPSJtYWlsdG86ZXRpY2tldEBhbWFkZXVzLmNvbSI+ZXRpY2tldEBhbWFkZXVzLmNvbTwvYT4mZ3Q7DQo8YnI+DQo8Yj5TZW50OjwvYj4gVGh1cnNkYXksIEFwcmlsIDksIDIwMjAgMTI6MzQgUE08YnI+DQo8Yj5Ubzo8L2I+IFBhcmlkaGkgVVBBREhZQVkgJmx0OzxhIGhyZWY9Im1haWx0bzpQYXJpZGhpLlVQQURIWUFZQGFtYWRldXMuY29tIj5QYXJpZGhpLlVQQURIWUFZQGFtYWRldXMuY29tPC9hPiZndDs8YnI+DQo8Yj5TdWJqZWN0OjwvYj4gVVBBREhZQVlFL1BBUklESEkgTVMgMjBBUFIgTEhSIENERzxvOnA+PC9vOnA+PC9wPg0KPC9kaXY+DQo8L2Rpdj4NCjxwIGNsYXNzPSJNc29Ob3JtYWwiPjxvOnA+Jm5ic3A7PC9vOnA+PC9wPg0KPGRpdiBzdHlsZT0iYm9yZGVyOnNvbGlkICM5QzY1MDAgMS4wcHQ7cGFkZGluZzoyLjBwdCAyLjBwdCAyLjBwdCAyLjBwdCI+DQo8cCBjbGFzcz0iTXNvTm9ybWFsIiBzdHlsZT0ibGluZS1oZWlnaHQ6MTIuMHB0O2JhY2tncm91bmQ6I0ZGRUI5QyI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMC4wcHQ7Y29sb3I6IzlDNjUwMCI+Q0FVVElPTjo8L3NwYW4+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMC4wcHQ7Y29sb3I6YmxhY2siPiBUaGlzIGVtYWlsIG9yaWdpbmF0ZWQgZnJvbSBvdXRzaWRlIG9mIHRoZSBvcmdhbml6YXRpb24uIERvIG5vdCBjbGljayBsaW5rcyBvciBvcGVuIGF0dGFjaG1lbnRzDQogdW5sZXNzIHlvdSByZWNvZ25pemUgdGhlIHNlbmRlciBhbmQga25vdyB0aGUgY29udGVudCBpcyBzYWZlLjxvOnA+PC9vOnA+PC9zcGFuPjwvcD4NCjwvZGl2Pg0KPHAgY2xhc3M9Ik1zb05vcm1hbCI+PG86cD4mbmJzcDs8L286cD48L3A+DQo8ZGl2Pg0KPHAgYWxpZ249ImNlbnRlciIgc3R5bGU9InRleHQtYWxpZ246Y2VudGVyIj48Yj48c3BhbiBzdHlsZT0iZm9udC1zaXplOjE4LjBwdDtmb250LWZhbWlseTomcXVvdDtBcmlhbCZxdW90OyxzYW5zLXNlcmlmO2NvbG9yOmJsdWUiPlVQQURIWUFZRS9QQVJJREhJIE1TIDIwQVBSIExIUiBDREc8bzpwPjwvbzpwPjwvc3Bhbj48L2I+PC9wPg0KPHByZT4tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS08bzpwPjwvbzpwPjwvcHJlPg0KPHByZT48bzpwPiZuYnNwOzwvbzpwPjwvcHJlPg0KPHByZT5UaGlzIGRvY3VtZW50IGlzIGF1dG9tYXRpY2FsbHkgZ2VuZXJhdGVkLjxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPlBsZWFzZSBkbyBub3QgcmVzcG9uZCB0byB0aGlzIG1haWwuPG86cD48L286cD48L3ByZT4NCjxwcmU+PG86cD4mbmJzcDs8L286cD48L3ByZT4NCjxwcmU+PG86cD4mbmJzcDs8L286cD48L3ByZT4NCjxwcmU+Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7IEVMRUNUUk9OSUMgVElDS0VUPG86cD48L286cD48L3ByZT4NCjxwcmU+Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7IFBBU1NFTkdFUiBJVElORVJBUlkgUkVDRUlQVDxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPjxvOnA+Jm5ic3A7PC9vOnA+PC9wcmU+DQo8cHJlPiBCUklUSVNIIEFJUldBWVMgUExDIChCQVNTKSZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyBEQVRFOiAwOSBBUFIgMjAyMDxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPiBSRVZFTlVFIE1BTkFHRU1FTlQuIFNFTExJTkcmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsgQUdFTlQ6IDgwMTk8bzpwPjwvbzpwPjwvcHJlPg0KPHByZT4gU1lTVEVNUy48bzpwPjwvbzpwPjwvcHJlPg0KPHByZT4gQVVTVFJBTEFTSUEgSEJBMiZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyBOQU1FOiBVUEFESFlBWUUvUEFSSURISSBNUzxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPiBMT05ET048bzpwPjwvbzpwPjwvcHJlPg0KPHByZT4gSUFUQSZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyA6IDkxNCAwMzkxMTxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPiBURUxFUEhPTkUmbmJzcDsgOiAwODQ1IDQ5MyAwIDc4NzxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPjxvOnA+Jm5ic3A7PC9vOnA+PC9wcmU+DQo8cHJlPiBJU1NVSU5HIEFJUkxJTkUmbmJzcDsgJm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7OiBCUklUSVNIIEFJUldBWVM8bzpwPjwvbzpwPjwvcHJlPg0KPHByZT4gVElDS0VUIE5VTUJFUiZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyA6IEVUS1QgMTI1IDIxMDYyNzQ4MDY8bzpwPjwvbzpwPjwvcHJlPg0KPHByZT4gQk9PS0lORyBSRUYgOiBBTUFERVVTOiBPM1ZNUFMsIEFJUkxJTkU6IEJBL08zVk1QUzxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPjxvOnA+Jm5ic3A7PC9vOnA+PC9wcmU+DQo8cHJlPiBGUk9NIC9UTyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyBGTElHSFQmbmJzcDsgQ0wgREFURSZuYnNwOyZuYnNwOyBERVAmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsgRkFSRSBCQVNJUyZuYnNwOyZuYnNwOyZuYnNwOyBOVkImbmJzcDsmbmJzcDsgTlZBJm5ic3A7Jm5ic3A7IEJBRyZuYnNwOyBTVDxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPjxvOnA+Jm5ic3A7PC9vOnA+PC9wcmU+DQo8cHJlPiBMT05ET04gSEVBVEhST1cgQkEgMzA0Jm5ic3A7IFYmbmJzcDsgMjBBUFImbmJzcDsgMDcyMCZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyBWWjBSTyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyAyMEFQUiAyMEFQUiAwUEMmbmJzcDsgT0s8bzpwPjwvbzpwPjwvcHJlPg0KPHByZT4gVEVSTUlOQUw6NTxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPiBQQVJJUyBDSEFSTEVTJm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7IEFSUklWQUwgVElNRTogMDkzNSZuYnNwOyZuYnNwOyBBUlJJVkFMIERBVEU6IDIwQVBSPG86cD48L286cD48L3ByZT4NCjxwcmU+IERFIEdBVUxMRTxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPiBURVJNSU5BTDoyQTxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPiBCT0FSRElORyBUSU1FOiAyMCBBUFJJTCAwNjo1MCAoU1VCSkVDVCBUTyBDSEFOR0UpPG86cD48L286cD48L3ByZT4NCjxwcmU+PG86cD4mbmJzcDs8L286cD48L3ByZT4NCjxwcmU+PG86cD4mbmJzcDs8L286cD48L3ByZT4NCjxwcmU+IEFUIENIRUNLLUlOLCBQTEVBU0UgU0hPVyBBIFBJQ1RVUkUgSURFTlRJRklDQVRJT04gQU5EIFRIRSBET0NVTUVOVCBZT1UgR0FWRTxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPiBGT1IgUkVGRVJFTkNFIEFUIFJFU0VSVkFUSU9OIFRJTUU8bzpwPjwvbzpwPjwvcHJlPg0KPHByZT48bzpwPiZuYnNwOzwvbzpwPjwvcHJlPg0KPHByZT4gQ0FSUlktT04gQkFHOjxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPiBQTEVBU0UgQ09OVEFDVCBZT1VSIEFHRU5ULjxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPjxvOnA+Jm5ic3A7PC9vOnA+PC9wcmU+DQo8cHJlPjxvOnA+Jm5ic3A7PC9vOnA+PC9wcmU+DQo8cHJlPiBCQUdHQUdFIFBST0hJQklURUQ6IE5PVCBBUFBMSUNBQkxFPG86cD48L286cD48L3ByZT4NCjxwcmU+IEVORE9SU0VNRU5UUyZuYnNwOyA6IE5PTlJFRi9IQk8gLVowUjxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPiBQQVlNRU5UJm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7IDogQ0E8bzpwPjwvbzpwPjwvcHJlPg0KPHByZT48bzpwPiZuYnNwOzwvbzpwPjwvcHJlPg0KPHByZT4gRkFSRSBDQUxDVUxBVElPTiZuYnNwOyZuYnNwOyA6TE9OIEJBIFBBUjEyOC4wNE5VQzEyOC4wNEVORCBST0UwLjc3MzE1MDxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPjxvOnA+Jm5ic3A7PC9vOnA+PC9wcmU+DQo8cHJlPiBBSVIgRkFSRSZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyA6IEdCUCZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyA5OS4wMDxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPiBUQVgmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsgOiBHQlAmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsgMTMuMDBHQiZuYnNwOyZuYnNwOyBHQlAmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsgMjAuNjRVQjxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPiBUT1RBTCZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyA6IEdCUCZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyAxMzIuNjQ8bzpwPjwvbzpwPjwvcHJlPg0KPHByZT48bzpwPiZuYnNwOzwvbzpwPjwvcHJlPg0KPHByZT48bzpwPiZuYnNwOzwvbzpwPjwvcHJlPg0KPHByZT5JTiBBQ0NPUkRBTkNFIFdJVEggVEhFIEdSRU5FTExFIExBVyBZT1UgQ0FOIERJU1BMQVkgVEhFIElORk9STUFUSU9OIFJFTEFURUQgVE88bzpwPjwvbzpwPjwvcHJlPg0KPHByZT5USEUgQ0FSQk9OIENPTlNVTUVEIDogQ0xJQ0sgSEVSRTxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPjxhIGhyZWY9Imh0dHBzOi8vY2xpY2t0aW1lLnN5bWFudGVjLmNvbS8zWVl1UTZyNzFLNG1kUXJybXZMMkpBMzZIMj91PUhUVFAlM0ElMkYlMkZXV1cuSUNBTy5JTlQlMkZFTlZJUk9OTUVOVEFMLVBST1RFQ1RJT04lMkZDQVJCT05PRkZTRVQlMkZQQUdFUyUyRkRFRkFVTFQuQVNQWCI+aHR0cHM6Ly9jbGlja3RpbWUuc3ltYW50ZWMuY29tLzNZWXVRNnI3MUs0bWRRcnJtdkwySkEzNkgyP3U9SFRUUCUzQSUyRiUyRldXVy5JQ0FPLklOVCUyRkVOVklST05NRU5UQUwtUFJPVEVDVElPTiUyRkNBUkJPTk9GRlNFVCUyRlBBR0VTJTJGREVGQVVMVC5BU1BYPC9hPjxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPjxvOnA+Jm5ic3A7PC9vOnA+PC9wcmU+DQo8cHJlPk5PVElDRTxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPkNBUlJJQUdFIEFORCBPVEhFUiBTRVJWSUNFUyBQUk9WSURFRCBCWSBUSEUgQ0FSUklFUiBBUkUgU1VCSkVDVCBUTyBDT05ESVRJT05TPG86cD48L286cD48L3ByZT4NCjxwcmU+T0YgQ0FSUklBR0UsIFdISUNIIEFSRSBIRVJFQlkgSU5DT1JQT1JBVEVEIEJZIFJFRkVSRU5DRS4gVEhFU0UgQ09ORElUSU9OUyBNQVk8bzpwPjwvbzpwPjwvcHJlPg0KPHByZT5CRSBPQlRBSU5FRCBGUk9NIFRIRSBJU1NVSU5HIENBUlJJRVIuPG86cD48L286cD48L3ByZT4NCjxwcmU+PG86cD4mbmJzcDs8L286cD48L3ByZT4NCjxwcmU+VEhFIEJSSVRJU0ggQUlSV0FZUyBGUkVFIENIRUNLRUQgQkFHR0FHRSBBTExPV0FOQ0UgSU5DTFVERVMgQkFHUyBVUCBUTzxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPjIzS0dTLzUxTEJTIEFORC9PUiBTUE9SVElORyBFUVVJUE1FTlQsIE1VU0lDQUwgSU5TVFJVTUVOVFMsIEZJTE08bzpwPjwvbzpwPjwvcHJlPg0KPHByZT5FUVVJUE1FTlQgQUxMIE1FQVNVUklORyA5MCBYIDc1IFggNDNDTSAvIDM1LjUgWCAyOS41IFggMTZJTlMuIEJBR1MgT1I8bzpwPjwvbzpwPjwvcHJlPg0KPHByZT5JVEVNUyBUSEFUIEFSRSBJTiBFWENFU1MgT0YgVEhFIEZSRUUgQUxMT1dBTkNFIEFORC9PUiBFWENFRUQgMjNLRy81MUxCPG86cD48L286cD48L3ByZT4NCjxwcmU+TUFZIEJFIFNVQkpFQ1QgVE8gRVhDRVNTIEFORC9PUiBPVkVSV0VJR0hUIENIQVJHRVMgQVQgQ0hFQ0stSU4uPG86cD48L286cD48L3ByZT4NCjxwcmU+PG86cD4mbmJzcDs8L286cD48L3ByZT4NCjxwcmU+Q0FCSU4gQkFHR0FHRSBESU1FTlNJT05TIE1VU1QgTk9UIEVYQ0VFRCA1NkNNIFg0NUNNIFggMjVDTSAvIDIySU5TIFg8bzpwPjwvbzpwPjwvcHJlPg0KPHByZT4xOElOUyBYIDEwSU5TIExBUFRPUCBPUiBIQU5EQkFHIElURU1TIE1VU1QgTk9UIEVYQ0VFRCA0MENNIFggMzBDTSBYPG86cD48L286cD48L3ByZT4NCjxwcmU+MTVDTS8xNklOUyBYIDEySU5TIFggNklOUy48bzpwPjwvbzpwPjwvcHJlPg0KPHByZT5WSVNJVCA8YSBocmVmPSJodHRwczovL2NsaWNrdGltZS5zeW1hbnRlYy5jb20vM0ZxdlA0UllLYXBXQ2IxNkpOanljN3E2SDI/dT1IVFRQJTNBJTJGJTJGV1dXLkJSSVRJU0hBSVJXQVlTLkNPTSI+aHR0cHM6Ly9jbGlja3RpbWUuc3ltYW50ZWMuY29tLzNGcXZQNFJZS2FwV0NiMTZKTmp5YzdxNkgyP3U9SFRUUCUzQSUyRiUyRldXVy5CUklUSVNIQUlSV0FZUy5DT008L2E+IEFORCBTRUFSQ0ggRk9SIEJBR0dBR0UgRk9SIE1PUkU8bzpwPjwvbzpwPjwvcHJlPg0KPHByZT5ERVRBSUxTLjxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPjxvOnA+Jm5ic3A7PC9vOnA+PC9wcmU+DQo8cHJlPlRIRSBJVElORVJBUlkvUkVDRUlQVCBDT05TVElUVVRFUyBUSEUgUEFTU0VOR0VSIFRJQ0tFVCBGT1IgVEhFIFBVUlBPU0VTIE9GPG86cD48L286cD48L3ByZT4NCjxwcmU+QVJUSUNMRSAzIE9GIFRIRSBXQVJTQVcgQ09OVkVOVElPTiwgRVhDRVBUIFdIRVJFIFRIRSBDQVJSSUVSIERFTElWRVJTIFRPIFRIRTxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPlBBU1NFTkdFUiBBTk9USEVSIERPQ1VNRU5UIENPTVBMWUlORyBXSVRIIFRIRSBSRVFVSVJFTUVOVFMgT0YgQVJUSUNMRSAzLjxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPjxvOnA+Jm5ic3A7PC9vOnA+PC9wcmU+DQo8cHJlPlBBU1NFTkdFUlMgT04gQSBKT1VSTkVZIElOVk9MVklORyBBTiBVTFRJTUFURSBERVNUSU5BVElPTiBPUiBBIFNUT1AgSU4gQTxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPkNPVU5UUlkgT1RIRVIgVEhBTiBUSEUgQ09VTlRSWSBPRiBERVBBUlRVUkUgQVJFIEFEVklTRUQgVEhBVCBJTlRFUk5BVElPTkFMPG86cD48L286cD48L3ByZT4NCjxwcmU+VFJFQVRJRVMgS05PV04gQVMgVEhFIE1PTlRSRUFMIENPTlZFTlRJT04sIE9SIElUUyBQUkVERUNFU1NPUiwgVEhFIFdBUlNBVzxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPkNPTlZFTlRJT04sIElOQ0xVRElORyBJVFMgQU1FTkRNRU5UUyAoVEhFIFdBUlNBVyBDT05WRU5USU9OIFNZU1RFTSksIE1BWSBBUFBMWTxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPlRPIFRIRSBFTlRJUkUgSk9VUk5FWSwgSU5DTFVESU5HIEFOWSBQT1JUSU9OIFRIRVJFT0YgV0lUSElOIEEgQ09VTlRSWS4mbmJzcDsgRk9SPG86cD48L286cD48L3ByZT4NCjxwcmU+U1VDSCBQQVNTRU5HRVJTLCBUSEUgQVBQTElDQUJMRSBUUkVBVFksIElOQ0xVRElORyBTUEVDSUFMIENPTlRSQUNUUyBPRjxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPkNBUlJJQUdFIEVNQk9ESUVEIElOIEFOWSBBUFBMSUNBQkxFIFRBUklGRlMsIEdPVkVSTlMgQU5EIE1BWSBMSU1JVCBUSEU8bzpwPjwvbzpwPjwvcHJlPg0KPHByZT5MSUFCSUxJVFkgT0YgVEhFIENBUlJJRVIuIFRIRVNFIENPTlZFTlRJT05TIEdPVkVSTiBBTkQgTUFZIExJTUlUIFRIRTxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPkxJQUJJTElUWU9GIEFJUiBDQVJSSUVSUyBGT1IgREVBVEggT1IgQk9ESUxZIElOSlVSWSBPUiBMT1NTIE9GIE9SIERBTUFHRSBUTzxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPkJBR0dBR0UsIEFORCBGT1IgREVMQVkuPG86cD48L286cD48L3ByZT4NCjxwcmU+PG86cD4mbmJzcDs8L286cD48L3ByZT4NCjxwcmU+VEhFIENBUlJJQUdFIE9GIENFUlRBSU4gSEFaQVJET1VTIE1BVEVSSUFMUywgTElLRSBBRVJPU09MUywgRklSRVdPUktTLCBBTkQ8bzpwPjwvbzpwPjwvcHJlPg0KPHByZT5GTEFNTUFCTEUgTElRVUlEUywgQUJPQVJEIFRIRSBBSVJDUkFGVCBJUyBGT1JCSURERU4uIElGIFlPVSBETyBOT1QgVU5ERVJTVEFORDxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPlRIRVNFIFJFU1RSSUNUSU9OUywgRlVSVEhFUiBJTkZPUk1BVElPTiBNQVkgQkUgT0JUQUlORUQgRlJPTSBZT1VSIEFJUkxJTkUuPG86cD48L286cD48L3ByZT4NCjxwcmU+PG86cD4mbmJzcDs8L286cD48L3ByZT4NCjxwcmU+REFUQSBQUk9URUNUSU9OIE5PVElDRTogWU9VUiBQRVJTT05BTCBEQVRBIFdJTEwgQkUgUFJPQ0VTU0VEIElOIEFDQ09SREFOQ0U8bzpwPjwvbzpwPjwvcHJlPg0KPHByZT5XSVRIIFRIRSBBUFBMSUNBQkxFIENBUlJJRVInUyBQUklWQUNZIFBPTElDWSBBTkQsIElGIFlPVVIgQk9PS0lORyBJUyBNQURFIFZJQTxvOnA+PC9vOnA+PC9wcmU+DQo8cHJlPkEgUkVTRVJWQVRJT04gU1lTVEVNIFBST1ZJREVSICggR0RTICksIFdJVEggSVRTIFBSSVZBQ1kgUE9MSUNZLiBUSEVTRSBBUkU8bzpwPjwvbzpwPjwvcHJlPg0KPHByZT5BVkFJTEFCTEUgQVQgPGEgaHJlZj0iaHR0cHM6Ly9jbGlja3RpbWUuc3ltYW50ZWMuY29tLzM1MTh4ZU5yenpTaU1iSzlvQ05qRTZiNkgyP3U9aHR0cCUzQSUyRiUyRnd3dy5pYXRhdHJhdmVsY2VudGVyLmNvbSUyRnByaXZhY3kiPmh0dHBzOi8vY2xpY2t0aW1lLnN5bWFudGVjLmNvbS8zNTE4eGVOcnp6U2lNYks5b0NOakU2YjZIMj91PWh0dHAlM0ElMkYlMkZ3d3cuaWF0YXRyYXZlbGNlbnRlci5jb20lMkZwcml2YWN5PC9hPiBPUiBGUk9NIFRIRSBDQVJSSUVSIE9SPG86cD48L286cD48L3ByZT4NCjxwcmU+R0RTIERJUkVDVExZLiBZT1UgU0hPVUxEIFJFQUQgVEhJUyBET0NVTUVOVEFUSU9OLCBXSElDSCBBUFBMSUVTIFRPIFlPVVI8bzpwPjwvbzpwPjwvcHJlPg0KPHByZT5CT09LSU5HIEFORCBTUEVDSUZJRVMsIEZPUiBFWEFNUExFLCBIT1cgWU9VUiBQRVJTT05BTCBEQVRBIElTIENPTExFQ1RFRCw8bzpwPjwvbzpwPjwvcHJlPg0KPHByZT5TVE9SRUQsIFVTRUQsIERJU0NMT1NFRCBBTkQgVFJBTlNGRVJSRUQuKEFQUExJQ0FCTEUgRk9SIElOVEVSTElORSBDQVJSSUFHRSk8bzpwPjwvbzpwPjwvcHJlPg0KPC9kaXY+DQo8L2Rpdj4NCjwvYm9keT4NCjwvaHRtbD4NCg0KLS1fMDAwX0FNMFBSMTBNQjIxOTNDOUI2NEI1MEM4MTcxMzdGMzQ1MUZDQzEwQU0wUFIxME1CMjE5M0VVUlBfLS0NCg=='

# Starts the parsing process
try:
    response = amadeus.travel.trip_parser_jobs.post(
        amadeus.travel.from_base64(booking_base64))
    print(response.data['id'])
except ResponseError as error:
    raise error