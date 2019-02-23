Sub Summary()

'Create Summary Page

    'Sheets.Add.Name = "Summary"
    'Sheets("Summary").Move Before:=Sheets("A")
    'Set combined_sheets = Worksheets("Summary")

'Define variables

    Dim Ticker As String
    Dim StockVolume As Double
    Dim SummaryRow As Integer
    Dim OpenTracker As Integer
    Dim OpenPrice As Double
    Dim OpenYr As Double
    Dim ClosePrice As Double
    Dim CloseYr As Double
    Dim YrChange As Double
    Dim PercentChange As Double
    OpenTracker = 0

'Create loop for worksheets and define starting variables

    For Each ws In Worksheets

'For each worksheet, reset tracker for Open price, volume to zero and summary table start to row 2
    
    StockVolume = 0
    OpenTracker = 0
    SummaryRow = 2
  
  
'Define and style header columns for summary table

    ws.Range("J1").Value = "Ticker"
    ws.Range("K1").Value = "Yearly Change"
    ws.Range("L1").Value = "Percent Change"
    ws.Range("M1").Value = "Total Stock Volume"
    ws.Columns("J:M").AutoFit

'Find the last row in the ticker column

    LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row

'create For loop to from row 2 to last row in each sheet

        For i = 2 To LastRow

'Define If statement

           If ws.Cells(i, 1).Value = ws.Cells(i + 1, 1).Value Then
             Ticker = ws.Cells(i, 1).Value

'add summary of stock volume to current row values

              StockVolume = StockVolume + ws.Cells(i, 7).Value

'Since the cells adjacent to each other are equal, start the open tracker
              
              OpenTracker = OpenTracker + 1
            
'Return the open price when the open date tracker is equal to 1 which means it is the first row after
'ticker reset on the last row

                 If OpenTracker = 1 Then
                    OpenPrice = ws.Cells(i, 3)
                    OpenYr = ws.Cells(i, 2)
          
                    Else

                 End If
           
            Else
'If the ticker type is the same as the ticker below, add to stock volume and add to Open date tracker
            
                StockVolume = StockVolume + ws.Cells(i, 7).Value

'place calculated variables in summary table

                ws.Range("J" & SummaryRow).Value = Ticker
                ws.Range("M" & SummaryRow).Value = StockVolume
            
'It adjacent rows <> each other, the next row is a different ticker, return close price

                ClosePrice = ws.Cells(i, 6)
                CloseYr = ws.Cells(i, 2)
                
'divide by zero to remove errors from dividing by zero

                If OpenPrice <> 0 Then
                   YrChange = ClosePrice - OpenPrice
                   PercentChange = (ClosePrice - OpenPrice) / OpenPrice
                Else
                   YrChange = 0
                   PercentChange = 0
                End If

'put Yearly Change and percent change in summary table
                ws.Range("K" & SummaryRow).Value = YrChange
                ws.Range("L" & SummaryRow).Value = PercentChange
                ws.Range("L" & SummaryRow).NumberFormat = "0.00%"

'Add conditional formatting to Yearly Change column: green for postitive chnages and red for negative
                If ws.Range("K" & SummaryRow).Value < 0 Then
                    ws.Range("K" & SummaryRow).Interior.Color = RGB(232, 12, 12)
                Else
                    ws.Range("K" & SummaryRow).Interior.Color = RGB(12, 183, 64)
                End If
 
'increase summaryRow total by one to put next ticker results on next row
                SummaryRow = SummaryRow + 1

'reset volume total and open price tracker

                StockVolume = 0
                OpenTracker = 0

             End If

'next iteration
          Next i
'next worksheet
      Next ws
End Sub



'Clear summary section data

Sub ClearContents()

Dim ws As Worksheet
Dim first_ws As Worksheet
Set first_ws = ActiveSheet


    For Each ws In ThisWorkbook.Worksheets
     ws.Activate
        
        Range("K:L").Interior.Color = xlNone
        Range("J:M").ClearContents

    Next

first_ws.Activate

End Sub
