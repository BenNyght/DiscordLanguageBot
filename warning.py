import re
from typing import Optional

WARNINGS = {
    # Sexist/exclusionary language
    r'\b(females)\b': 'pretty objectifying. If you are referring to women, use the gender term instead',
    r'\b(hysterical)\b': 'sexist language. Some alternatives: hilarious, funny',

    # Mental conditions
    r'\b(stupid|retarded|idiotic)\b': 'ableist language. Some alternatives: pathetic, uninspiring, vapid, obtuse, silly',
    r'\b(crazy|insane|bonkers)\b': 'ableist language. Some alternatives: ludicrous, wild, ridiculous, absurd, chaotic, silly, nonsensical, unreal, unbelievable',
    r'\b(mad)\b': 'ableist language. Some alternatives: angry, furious, annoyed',
    r'\b(idiot|idiotic|imbecile|moron|retard|lunatic)\b': 'ableist language. Some alternatives: uninformed, ignorant, incorrect, wrong',

    # Physical conditions
    r'\b(dumb)\b': 'ableist language. Some alternatives: silly, foolish, ignorant, uninformed, ridiculous, pathetic, absurd',
    r'\b(lame)\b': 'ableist language. Some alternatives: silly, foolish, ridiculous, pathetic, absurd, uncool',
    r'\b(cripple|crippled)\b': 'ableist language. Some alternatives: broken, not working',

    # Racism
    r'\b(gypsy)\b': 'a racial slur against the Romani people.',
    r'\b(nigger|nigga|negro)\b': 'a racial slur against black people.',

    # catchall ableist (No suggestions)
    r'\b(psycho|schitzo|schizo|spaz|derp|spastic|spacker)\b': 'ableist language. check out some alternatives! <http://www.autistichoya.com/p/ableist-words-and-terms-to-avoid.html> (scroll down)',
}

def get_warning(text):
    for key in WARNINGS:
        warning = re.search(key, text, re.IGNORECASE)
        if warning:
            return 'Friendly Reminder: {0} is {1}'.format(warning.group(0), WARNINGS[key])
    return None
