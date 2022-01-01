# Make tokens and lexicons for speech2text using flashlight.asr
1. clean lst and make full transcript text
2. Create lexicon  
```
python create_token/create_token.py -p 8 --wp 7199 -t <path_to-full_text>  -d <path_to_dictionany>
```