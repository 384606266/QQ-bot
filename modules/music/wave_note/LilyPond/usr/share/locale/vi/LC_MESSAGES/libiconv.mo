??    ,      |  ;   ?      ?  C   ?  9     o   G  B   ?  m   ?  ?   h  \   ?  ;     P   A  [   ?     ?  @   ?  N   2  J   ?  D   ?  d     :   v     ?     ?     ?  0   ?     	  5   	  	   P	     Z	  )   o	  "   ?	  1   ?	  +   ?	  ?   
  &   ?
  A   ?
  ;        W  /   g  3   ?  :   ?  $        +     J     g     u  2   ?  o  ?  a   (  K   ?  ?   ?  W   `  ?   ?  O   C  j   ?  O   ?  ]   N  h   ?       V     i   o  d   ?  a   >  ~   ?  :        Z     r  &   {  ;   ?     ?  J   ?     G     [  >   o  5   ?  B   ?  2   '  ?   Z  J     ]   \  P   ?       B     I   _  O   ?  =   ?  5   7  5   m     ?     ?  V   ?               $   	       (          
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
 or:    iconv -l try '%s -l' to get the list of supported encodings Project-Id-Version: libiconv-1.11-pre1
Report-Msgid-Bugs-To: bug-gnu-libiconv@gnu.org
POT-Creation-Date: 2006-07-19 21:16+0200
PO-Revision-Date: 2006-06-23 16:38+0930
Last-Translator: Clytie Siddall <clytie@riverland.net.au>
Language-Team: Vietnamese <vi-VN@googlegroups.com> 
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
   --byte-subst=CHUỖI_DẠNG_THỨC
						sư thay thế các byte không thể chuyển đổi
   --help                      hiển thị _trợ giúp_ này rồi thoát
   --unicode-subst=CHUỖI_DẠNG_THỨC
                              sự thay thế các ký tự Unicode không thể chuyển đổi
   --version                   hiển thị thông tin về _phiên bản_ rồi thoát
   --widechar-subst=CHUỖI_DẠNG_THỨC
                             		sự thay thế các ký tự rộng không thể chuyển đổi
   -c                          hủy các ký tự không thể chuyển đổi
   -f BẢNG_MÃ, --from-code=BẢNG_MÃ
                              bảng mã của dữ liệu nhập
   -l, --list                  _liệt kê_ các bảng mã được hỗ trợ
   -s, --silent                thu hồi các thông điệp về vấn đề chuyển đổi
   -t BẢNG_MÃ, --to-code=BẢNG_MÃ
                              bảng mã của dữ liệu xuất
 %s Đối số %s: ở đây không cho phép chỉ thị dạng thức với kích cỡ. Đối số %s: ở đây không cho phép chỉ thị dạng thức với độ chính xác thay đổi. Đối số %s: ở đây không cho phép chỉ thị dạng thức với độ rộng thay đổi. Đối số %s: ký tự « %c » không phải là bộ xác định chuyển đổi hợp lệ. Đối số %s: ký tự kết thúc chỉ thị dạng thức không phải là bộ xác định chuyển đổi hợp lệ. Đối số %s: chuỗi kết thúc ở trong chỉ thị. %s: lỗi nhập/xuất %s:%u:%u %s:%u:%u: không thể chuyển đổi %s:%u:%u: dây kiểu ký tự hay dịch chưa hoàn toàn (thiết bị nhập chuẩn) Chuyển đổi đoạn chữ từ bảng mã này sang bảng mã khác.
 Lỗi nhập/xuất Xuất thông tin:
 Các tùy chọn điều khiển vấn đề chuyển đổi:
 Các tùy chọn điều khiển cách xuất lỗi:
 Các tùy chọn điều khiển dạng thức nhập và xuất:
 Thông báo lỗi cho <bug-gnu-libiconv@gnu.org>.
 Phần mềm này là tự do; hãy xem mã nguồn để tìm điều kiện sao chép.
KHÔNG bảo đảm gì cả, dù khả năng bán hay khả năng làm việc dứt khoát.
 Hãy thử lệnh trợ giúp « %s --help » để xem thông tin thêm.
 Cách sử dụng: %s [TÙY_CHỌN...] [-f BẢNG_MÃ] [-t BẢNG_MÃ] [TẬP_TIN_NHẬP...]
 Cách sử dụng: iconv [-c] [-s] [-f từ_mã] [-t đến_mã] [tập_tin ...] Tác giả: %s.
 không thể chuyển đổi sự thay thế byte sang Unicode: %s không thể chuyển đổi sự thay thế byte sang chuỗi rộng: %s không thể chuyển đổi sự thay thế Unicode sang bảng mã đích: %s không hỗ trợ khả năng chuyển đổi từ %s sang %s không hỗ trợ khả năng chuyển đổi từ %s không hỗ trợ khả năng chuyển đổi sang %s hay:    %s -l
 hay:    iconv -l hãy thử lệnh « %s -l » để xem danh sách các bảng mã được hỗ trợ 