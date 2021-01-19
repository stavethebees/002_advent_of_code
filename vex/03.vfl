void format(string input; string output[])
{
    string _tokenized[] = split(input, "\n");
    foreach (string _s; _tokenized)
    {
          _s = strip(_s);
          append(output, _s);
    }
}


int traverse(string input[]; int x; int y)
{
    int _height = len(input);
    int _width = len(input[0]);
    int _trees = 0;
        
    int _currenty = 0;
    int _currentx = 0;
    
    while(_currenty <= _height)
    {
        _currentx += x;
        _currentx %= _width;
        _currenty += y;
        string _currentlevel = input[_currenty];
        if (_currentlevel[_currentx] == "#")
            _trees++;  
    }
    return _trees;
}


// main
s[]@sorted;
format(s@input_orig, @sorted);
i@__resultPART1 = traverse(@sorted, 3, 1);


vector2 _inputarray[] = array({1,1}, {3,1}, {5,1}, {7, 1}, {1, 2});
int _sums[];
for (int i = 0; i < len(_inputarray); i++)
{
    vector2 _traversal = _inputarray[i];
    int _num = traverse(@sorted, int(_traversal.x), int(_traversal.y));
    append(_sums, _num);
}

i[]@sums = _sums;
float _trees = _sums[0];
for(int i = 1; i < len(_sums); i++)
{
    _trees *= (float(_sums[i]));
}
@__resultPART2 = _trees;