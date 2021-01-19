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

function int[] format(const string input)
{
    int _output[];
    string _tokenized[] = split(input, "\n");
    foreach (string _s; _tokenized)
    {
          _s = strip(_s);
          append(_output, atoi(_s));
    }
    return _output;
}


// main
int _numarray[] = format(s@inputorig);
sort(_numarray);
int _sum = 2020;
int _first, _second, _third, _result;

for (int i = 0; i < len(_numarray); i++)
{
    for (int j = i; j < len(_numarray); j++)
    {
        _first = _numarray[i];
        _second = _numarray[j];
        if (_first + _second == _sum)
        {
            _result = _first * _second;
            break;
        }
    }
}
i@__result_PART1 = _result;


for (int i = 0; i < len(_numarray); i++)
{
    for (int j = i; j < len(_numarray); j++)
    {
        for (int k = j; k < len(_numarray); k++)
        {
            _first = _numarray[i];
            _second = _numarray[j];
            _third = _numarray[k];
            if (_first + _second + _third == _sum)
            {
                _result = _first * _second * _third;
                break;
            }
        }
    }
}
i@__result_PART2 = _result;
