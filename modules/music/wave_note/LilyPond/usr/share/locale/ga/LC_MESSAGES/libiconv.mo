??    ,      |  ;   ?      ?  C   ?  9     o   G  B   ?  m   ?  ?   h  \   ?  ;     P   A  [   ?     ?  @   ?  N   2  J   ?  D   ?  d     :   v     ?     ?     ?  0   ?     	  5   	  	   P	     Z	  )   o	  "   ?	  1   ?	  +   ?	  ?   
  &   ?
  A   ?
  ;        W  /   g  3   ?  :   ?  $        +     J     g     u  2   ?    ?  C   8  C   |  k   ?  F   ,  l   s  H   ?  W   )  J   ?  W   ?  T   $     y  =   |  N   ?  N   	  B   X  h   ?  1        6     F     O  ,   j     ?  $   ?     ?     ?  +   ?  (     3   ;  ;   o  ?   ?  :   k  @   ?  5   ?       4   %  =   Z  E   ?  "   ?               <     J  U   Z               $   	       (          
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
PO-Revision-Date: 2006-07-16 14:58-0500
Last-Translator: Kevin Patrick Scannell <scannell@SLU.EDU>
Language-Team: Irish <gaeilge-gnulinux@lists.sourceforge.net>
MIME-Version: 1.0
Content-Type: text/plain; charset=ISO-8859-1
Content-Transfer-Encoding: 8bit
   --byte-subst=TEAGHR?N       ionada?ocht do bhearta dothiontaithe
   --help                      taispe?in an chabhair seo agus scoir
   --unicode-subst=TEAGHR?N
                              ionada?ocht do charachtair dhothiontaithe Unicode
   --version                   taispe?in eolas faoin leagan agus scoir
   --widechar-subst=TEAGHR?N
                             ionada?ocht do charachtair leathana dhothiontaithe
   -c                        caith carachtair dhothiontaithe i dtraipis?
   -f IONCH?D?, --from-code=IONCH?D?
                              ionch?d? an ionchuir
   -l, --list                  taispe?in na hionch?duithe a dtaca?tear leo
   -s, --silent                n? taispe?in teachtaireachta? faoi fhadhbanna tiontaithe
   -t IONCH?D?, --to-code=IONCH?D?
                              ionch?d? an aschuir
 %s arg?int %s: N? cheada?tear treoir fhorm?idithe le m?id anseo. arg?int %s: N? cheada?tear treoir fhorm?idithe le beachtas athraitheach anseo. arg?int %s: N? cheada?tear treoir fhorm?idithe le leithead athraitheach anseo. arg?int %s: N?l carachtar '%c' bail? mar shonraitheoir tiontaithe. arg?int %s: An carachtar ag deireadh na treorach form?idithe, n?l s? bail? mar shonraitheoir tiontaithe. arg?int %s: Deireadh an teaghr?in i l?r treorach. %s: Earr?id I/A %s:%u:%u %s:%u:%u: n? f?idir tiont? %s:%u:%u: carachtar n? seicheamh neamhioml?n (stdin) Tiontaigh ? ionch?d? go ceann eile.
 Earr?id I/A Aschur faisn?iseach:
 Roghanna a riala?onn fadhbanna tiontaithe:
 Roghanna a riala?onn aschur d'earr?id?:
 Roghanna a riala?onn form?id ionchurtha/aschurtha:
 Seol tuairisc? fabhtanna chuig <bug-gnu-libiconv@gnu.org>.
 Is saorbhogearra an r?omhchl?r seo; f?ach ar an bhunch?d le haghaidh
coinn?ollacha c?ipe?la.  N?l bar?nta ar bith ann; go fi? n?l bar?nta ann
d'IND?OLTACHT n? FEILI?NACHT D'FHEIDHM AR LEITH.
 Bain triail as `%s --help' chun tuilleadh eolais a fh?il.
 ?s?id: %s [ROGHA...] [-f IONCH?D?] [-t IONCH?D?] [INCHOMHAD...]
 ?s?id: iconv [-c] [-s] [-f c?d] [-t c?d] [comhad ...] Le %s.
 n? f?idir ionada?ocht bhirt a thiont? go Unicode: %s n? f?idir ionada?ocht bhirt a thiont? go teaghr?n leathan: %s n? f?idir ionada?ocht unicode a thiont? go dt? an sprioc-ionch?d?: %s n? thaca?tear le tiont? ? %s go %s n? thaca?tear le tiont? ? %s n? thaca?tear le tiont? go %s n?:    %s -l
 n?:    iconv -l bain triail as '%s -l' chun liosta de na hionch?duithe a dtaca?tear leo a thaispe?int 