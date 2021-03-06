??    ,      |  ;   ?      ?  C   ?  9     o   G  B   ?  m   ?  ?   h  \   ?  ;     P   A  [   ?     ?  @   ?  N   2  J   ?  D   ?  d     :   v     ?     ?     ?  0   ?     	  5   	  	   P	     Z	  )   o	  "   ?	  1   ?	  +   ?	  ?   
  &   ?
  A   ?
  ;        W  /   g  3   ?  :   ?  $        +     J     g     u  2   ?    ?  E   8  ?   ~  j   ?  E   )  j   o  ?   ?  N     9   i  L   ?  L   ?     =  :   @  D   {  C   ?  <     V   A  7   ?     ?     ?     ?  2   	     <  ,   L     y     ?  '   ?  %   ?  1   ?  .     ?   H  '   ?  :     ?   @     ?  0   ?  :   ?  4   ?  #   1     U     s     ?     ?  0   ?               $   	       (          
   )                                 '              %                                #   &                   "   ,                               +         *       !         --byte-subst=FORMATSTRING   substitution for unconvertible bytes
   --help                      display this help and exit
   --unicode-subst=FORMATSTRING
                              substitution for unconvertible Unicode characters
   --version                   output version information and exit
   --widechar-subst=FORMATSTRING
                              substitution for unconvertible wide characters
   -c                          discard unconvertible characters
   -f ENCODING, --from-code=ENCODING
                              the encoding of the input
   -l, --list                  list the supported encodings
   -s, --silent                suppress error messages about conversion problems
   -t ENCODING, --to-code=ENCODING
                              the encoding of the output
 %s %s argument: A format directive with a size is not allowed here. %s argument: A format directive with a variable precision is not allowed here. %s argument: A format directive with a variable width is not allowed here. %s argument: The character '%c' is not a valid conversion specifier. %s argument: The character that terminates the format directive is not a valid conversion specifier. %s argument: The string ends in the middle of a directive. %s: I/O error %s:%u:%u %s:%u:%u: cannot convert %s:%u:%u: incomplete character or shift sequence (stdin) Converts text from one encoding to another encoding.
 I/O error Informative output:
 Options controlling conversion problems:
 Options controlling error output:
 Options controlling the input and output format:
 Report bugs to <bug-gnu-libiconv@gnu.org>.
 This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 Try `%s --help' for more information.
 Usage: %s [OPTION...] [-f ENCODING] [-t ENCODING] [INPUTFILE...]
 Usage: iconv [-c] [-s] [-f fromcode] [-t tocode] [file ...] Written by %s.
 cannot convert byte substitution to Unicode: %s cannot convert byte substitution to wide string: %s cannot convert unicode substitution to target encoding: %s conversion from %s to %s unsupported conversion from %s unsupported conversion to %s unsupported or:    %s -l
 or:    iconv -l try '%s -l' to get the list of supported encodings Project-Id-Version: libiconv 1.11-pre1
Report-Msgid-Bugs-To: bug-gnu-libiconv@gnu.org
POT-Creation-Date: 2006-07-19 21:16+0200
PO-Revision-Date: 2006-07-02 10:42+0100
Last-Translator: Edmund GRIMLEY EVANS <edmundo@rano.org>
Language-Team: Esperanto <translation-team-eo@lists.sourceforge.net>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
   --byte-subst=FORMATĈENO     substituado de nekonverteblaj bitokoj
   --help                      montri ĉi tiun helpon kaj eliri
   --unicode-subst=FORMATĈENO
                              substituado de nekonverteblaj unikodaj signoj
   -version                    eligi informon pri la versio kaj eliri
   --widechar-subst=FORMATĈENO
                              substituado de nekonverteblaj larĝaj signoj
   -c                          forĵeti nekonverteblajn signojn
   -f KODO, --from-code=KODO
                              la kodo de la enigo
   -l, --list                  listigi la konatajn kodojn
   -s, --silent                subpremi eraromesaĝojn pri konvertoproblemoj
   -t KODO, --to-code=KODO
                              la kodo de la eligo
 %s %s argumento: Formatdirektivo kun grando ne eblas ĉi tie. %s argumento: Formatdirektivo kun variabla precizo ne eblas ĉi tie. %s argumento: Formatdirektivo kun variabla larĝo ne eblas ĉi tie. %s argumento: La signo '%c' ne estas valida konvertospecifo. %s argumento: La signo, kiu finas la formatdirektivon ne estas valida konvertospecifo. %s argumento: La signoĉeno finiĝas meze de direktivo. %s: leg/skrib-eraro %s:%u:%u %s:%u:%u: ne povas konverti %s:%u:%u: malkompleta signo aŭ reĝimŝanĝa kodo (normala enigo) Konvertas tekston de unu kodo al alia kodo.
 leg/skrib-eraro Informa eligo:
 Opcioj, kiuj regas konvertoproblemojn:
 Opcioj, kiuj regas eligon de eraroj:
 Opcioj, kiuj regas la formon de enigo kaj eligo:
 Raportu cimojn al <bug-gnu-libiconv@gnu.org>.
 Ĉi tio estas libera programo; vidu la fonton por kopikondiĉoj. Estas NENIA
garantio; eĉ ne por KOMERCA KVALITO aŭ ADEKVATECO POR DIFINITA CELO.
 Provu '%s --help' por pli da informoj.
 Uzado: %s [OPCIO...] [-f KODO] [-t KODO] [ENIGDOSIERO...]
 Uzado: iconv [-c] [-s] [-f fontkodo] [-t celkodo] [dosiero ...] Verkita de %s.
 ne povas konverti bitoksubstituon al Unikodo: %s ne povas konverti bitoksubstituon al larĝa signoĉeno: %s ne povas konverti unikodan substituon al celkodo: %s konvertado de %s al %s ne disponata konvertado de %s ne disponata konvertado al %s ne disponata aŭ:    %s -l
 aŭ:    iconv -l provu '%s -l' por ricevi liston de konataj kodoj 