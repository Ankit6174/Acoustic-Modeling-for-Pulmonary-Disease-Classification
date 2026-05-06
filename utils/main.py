import librosa

def get_length(audio_path: str = None):
    """
    Return the length of an audio file path in seconds.

    Args:
        audio_path (str): Full path of an audio file.

    Return:
        len (int): Length of an audio file
    """
    assert (audio_path is not None), "Audio file path is required!"
    
    waveform, sr = librosa.load(audio_path)

    return (waveform.shape[0] / sr)

def get_cycle_info(txt_path: str = None):
    """
    Return all the resperatory cycle information of a perticular petient.

    Args:
        txt_path (str): Complete path of text file of related patient.

    Return:
        {
            beginning_of_respiratory (list): Beginning of respiratory cycle(s) 
            end_of_respiratory (list): End of respiratory cycle(s) 
            crackles (list): Presence/absence of crackles (presence=1, absence=0) 
            wheezes (list): Presence/absence of wheezes (presence=1, absence=0) 
        }
    """
    
    assert (txt_path is not None), "Text file path is required!"

    beginning_of_respiratory = []
    end_of_respiratory = []
    crackles = []
    wheezes = []
    
    with open(txt_path) as file:
        f = file.read()
        lines = f.split('\n')
        
        for line in lines:
            values = line.split('\t')
            if len(values) == 4:
                beginning_of_respiratory.append(values[0])
                end_of_respiratory.append(values[1])
                crackles.append(values[2])
                wheezes.append(values[3])
                
    return {
        "beginning_of_respiratory": beginning_of_respiratory,
        "end_of_respiratory": end_of_respiratory,
        "crackles": crackles,
        "wheezes": wheezes
    }