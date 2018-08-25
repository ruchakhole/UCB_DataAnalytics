
Sub stock_analysis():

' Set dimensions Dim total As Double Dim i As Long Dim change As Single 
Dim j As Integer 
Dim Begin As Long 
Dim rowCount As Long 
Dim percentChange As Double 
Dim days As Integer 
Dim dailyChange As Single 
Dim averageChange As Single 
Dim ws As Worksheet

For Each ws In Worksheets

j = 0
total = 0
change_price = 0
Begin = 2
dailyChange = 0


ws.Range("I1").Value = "Ticker"
ws.Range("J1").Value = "Yearly Change"
ws.Range("K1").Value = "Percent Change"
ws.Range("L1").Value = "Total Stock Volume"
ws.Range("P1").Value = "Ticker"
ws.Range("Q1").Value = "Value"
ws.Range("O2").Value = "Greatest % Increase"
ws.Range("O3").Value = "Greatest % Decrease"
ws.Range("O4").Value = "Greatest Total Volume"

rowCount = Cells(Rows.Count, "A").End(xlUp).Row

    For i = 2 To rowCount

        If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then

            total = total + ws.Cells(i, 7).Value

            If total = 0 Then

                ws.Range("I" & 2 + j).Value = Cells(i, 1).Value
                ws.Range("J" & 2 + j).Value = 0
                ws.Range("K" & 2 + j).Value = "%" & 0
                ws.Range("L" & 2 + j).Value = 0
            Else

            If ws.Cells(Begin, 3) = 0 Then
                For find_value = Begin To i
                    If ws.Cells(find_value, 3).Value <> 0 Then
                        Begin = find_value
                        Exit For
                    End If
                Next find_value
            End If

            change_price = (ws.Cells(i, 6) - ws.Cells(Begin, 3))
            percentChange = Round((change_price / ws.Cells(Begin, 3) * 100), 2)

            Begin = i + 1

            ws.Range("I" & 2 + j).Value = ws.Cells(i, 1).Value
            ws.Range("J" & 2 + j).Value = Round(change_price, 2)
            ws.Range("K" & 2 + j).Value = "%" & percentChange
            ws.Range("L" & 2 + j).Value = total

' Select Case is an alternative to IF function. I did not want to run a lot of If functions to avoid confusion for my sake.
            Select Case change_price
                Case Is > 0
                ws.Range("J" & 2 + j).Interior.ColorIndex = 4
                Case Is < 0
                    ws.Range("J" & 2 + j).Interior.ColorIndex = 3
                Case Else
                    ws.Range("J" & 2 + j).Interior.ColorIndex = 0
            End Select
            
        End If

            total = 0
            change_price = 0
            j = j + 1
            days = 0
            dailyChange = 0

        Else
            total = total + ws.Cells(i, 7).Value

        End If

    Next i

    ws.Range("Q2") = "%" & WorksheetFunction.Max(ws.Range("K2:K" & rowCount)) * 100
    ws.Range("Q3") = "%" & WorksheetFunction.Min(ws.Range("K2:K" & rowCount)) * 100
    ws.Range("Q4") = WorksheetFunction.Max(ws.Range("L2:L" & rowCount))

    ' returns one less because header row not a factor
    increase_number = WorksheetFunction.Match(WorksheetFunction.Max(ws.Range("K2:K" & rowCount)), ws.Range("K2:K" & rowCount), 0)
    decrease_number = WorksheetFunction.Match(WorksheetFunction.Min(ws.Range("K2:K" & rowCount)), ws.Range("K2:K" & rowCount), 0)
    volume_number = WorksheetFunction.Match(WorksheetFunction.Max(ws.Range("L2:L" & rowCount)), ws.Range("L2:L" & rowCount), 0)

    ws.Range("P2") = ws.Cells(increase_number + 1, 9)
    ws.Range("P3") = ws.Cells(decrease_number + 1, 9)
    ws.Range("P4") = ws.Cells(volume_number + 1, 9)

Next ws
End Sub