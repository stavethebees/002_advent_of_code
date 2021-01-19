function string[] format(const string input)
{
    string _output[];
    string _tokenized[] = split(input, "\n");
    foreach (string _s; _tokenized)
    {
          _s = strip(_s);
          append(_output, _s);
    }
    return _output;
}


function int[] traverse(int start; int end; const string instruction)
{
    int _length = end - start;
    int _pos[];
    if (instruction == "F" || instruction == "L")
    {
        _pos[0] = start;
        _pos[1] = start + _length/2;
    }
    else
    {
        _pos[0] = start + _length/2 + 1;
        _pos[1] = end;
    }
    
    return _pos;
}


// main
string _result0[] = format(s@inputorig);
int _rows = 128;
int _columns = 8;
int _seatIDs[];

foreach (string _s; _result0)
{
    // split row and column instructions
    string _instructions1 = _s[:-3];
    string _instructions2 = _s[-3:];
    
    int _start = 0;
    int _end = _rows - 1;
    int _row[] = array(_start, _end);
    
    while (len(_instructions1) > 0)
    {
        _row = traverse(_start, _end, _instructions1[0]);
        _start = _row[0];
        _end = _row[1];
        _instructions1 = _instructions1[1:];
    }
    
    _start = 0;
    _end = _columns - 1;
    
    int _column[] = array(_start, _end);
    while (len(_instructions2) > 0)
    {
        _column = traverse(_start, _end, _instructions2[0]);
        _start = _column[0];
        _end = _column[1];
        _instructions2 = _instructions2[1:];
    }
    int _seatID = _row[0] * 8 + _column[0];
    append(_seatIDs, _seatID);
}
i[]@seatIDs = reverse(sort(_seatIDs));
i@__resultPART1 = @seatIDs[0];


int _candidate = @seatIDs[0];
foreach(int _id; @seatIDs)
{
    if (_candidate != _id)
        break;
     _candidate--;
}
i@__resultPART2 = _candidate;