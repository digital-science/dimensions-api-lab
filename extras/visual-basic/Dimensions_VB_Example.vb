' example kindly provided by Timothy Cribbin <timothy.cribbin@brunel.ac.uk>

Module Module1

    Sub Main()
        ' Declare credential variables
        Dim UserName As String, PassWord As String, Token As String
        ' Declare and set the intended DSL query
        Dim DSLQuery As String = "search publications return publications"

        ' Input user credentials
        Console.WriteLine("Enter username ->")
        userName = Console.ReadLine()
        Console.WriteLine("Enter password ->")
        passWord = Console.ReadLine()
        Dim Login As String = "{""username"":""" & userName & """,""password"":""" & passWord & """}"

        ' Set up request to login URL to retrieve token
        Dim Req As Net.HttpWebRequest = CType(Net.HttpWebRequest.Create("https://app.dimensions.ai/api/auth.json"), Net.HttpWebRequest)
        Req.Method = "POST"
        Req.Timeout = 5000
        Req.ContentLength = Login.Length

        ' Write the Login details to the request body
        Using Body As New IO.StreamWriter(Req.GetRequestStream)
            Body.Write(Login)
        End Using

        ' Send Request, outputting the return code/message and ending the execution if there's an error
        Dim Resp As Net.WebResponse
        Try
            Resp = Req.GetResponse
        Catch ex As Exception
            Console.WriteLine(ex.Message)
            Do While Console.KeyAvailable = False
            Loop
            End
        End Try

        ' If successful response then read Token
        Using RStream As New IO.StreamReader(Resp.GetResponseStream)
            token = RStream.ReadToEnd().Split(":"c)(1).Trim({Chr(34), Chr(32), "}"c})
            Console.WriteLine("Token retrieved: " & token)
        End Using

        ' Create http request for the query and set the header using the generated token
        Req = CType(Net.HttpWebRequest.Create("https://app.dimensions.ai/api/dsl.json"), Net.HttpWebRequest)
        Req.Method = "POST"
        Req.Headers("Authorization") = "JWT " & Token
        Req.ContentLength = DSLQuery.Length

        ' Write the query to the request body
        Using Body As New IO.StreamWriter(Req.GetRequestStream)
            Body.Write(DSLQuery)
        End Using

        ' Send request, outputting the return code/message if there's an error
        Try
            Resp = Req.GetResponse
            Using RStream As New IO.StreamReader(Resp.GetResponseStream)
                Console.WriteLine(RStream.ReadToEnd)
            End Using
        Catch ex As Exception
            Console.WriteLine(ex.Message)
        End Try
        Do While Console.KeyAvailable = False
        Loop
        End
    End Sub

End Module
