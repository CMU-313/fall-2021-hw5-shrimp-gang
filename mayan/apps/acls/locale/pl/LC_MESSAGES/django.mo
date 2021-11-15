��    +      t  ;   �      �     �  
   �  �   �     �  �   �  I   6     �     �     �     �  Z   �     )  U   ?     �     �  �   �  	   �     �     �     �     �     �            !  G   8  <   �  	   �     �     �  K   �  F   +	  D   r	     �	     �	     �	  -   �	  .   
     E
  $   K
  !   p
  9   �
  	   �
    �
     �     �  �     	      b   
  D   m     �     �     �     �  t        {  n   �             �        �          .     J  !   `     �     �     �  N   �  M     
   Z     e     q  <   }  U   �  K        \     y     �  4   �  -   �     �  .        0  9   P     �                                    "                              *         $                 &   	            #          (   !                  )             +                  %   
       '                  ACL created ACL edited ACL stands for Access Control List and is a precise method to control user access to objects in the system. ACLs allow granting a permission to a role but only for a specific object or set of objects. ACLs API URL pointing to a permission in relation to the access control list to which it is attached. This URL is different than the canonical workflow URL. API URL pointing to the list of permissions for this access control list. Access control lists Access control lists for: %s Access entries Access entry An ACL for "%(object)s" using role "%(role)s" already exists. Edit that ACL entry instead. Available permissions Comma separated list of permission primary keys to grant to this access control list. Delete Delete ACL: %s Disabled permissions are inherited from a parent object or directly granted to the role and can't be removed from this view. Inherited permissions need to be removed from the parent object's ACL or from them role via the Setup menu. Edit ACLs Grant document access Grant object access Granted permissions Insufficient access for: %s New ACL New access control lists for: %s No such permission: %s Numeric identifier of the object for which the access will be modified. Object "%s" is not a model and cannot be checked for access. Object ID Object type Permissions Permissions to grant/revoke to/from the role for the object selected above. Primary key of the new permission to grant to the access control list. Primary keys of the role to which this access control list binds to. Revoke document access Revoke object access Role Role "%(role)s" permission's for "%(object)s" Role "%(role)s" permission's for "%(object)s". Roles Roles whose access will be modified. There are no ACLs for this object Type of the object for which the access will be modified. View ACLs Project-Id-Version: Mayan EDMS
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2020-05-18 09:57+0000
Last-Translator: Tomasz Szymanowicz <alakdae@gmail.com>
Language-Team: Polish (http://www.transifex.com/rosarior/mayan-edms/language/pl/)
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Language: pl
Plural-Forms: nplurals=4; plural=(n==1 ? 0 : (n%10>=2 && n%10<=4) && (n%100<12 || n%100>14) ? 1 : n!=1 && (n%10>=0 && n%10<=1) || (n%10>=5 && n%10<=9) || (n%100>=12 && n%100<=14) ? 2 : 3);
 Utworzono listę ACL Wyedytowano listę ACL ACL to skrót od Access Control List i jest precyzyjną metodą kontrolowania dostępu użytkowników do obiektów w systemie. Listy ACL pozwalają na przyznanie uprawnienia do roli, ale tylko dla określonego obiektu lub zestawu obiektów. Listy ACL API URL prowadzący do uprawnienia w liście kontroli dostępu, w której uprawnienie występuje.  API URL prowadzący do listy uprawnień dla listy kontroli dostępu. Listy kontroli dostępu Listy ACL dla: %s Zgłoszenia dostępu Zgłoszenie dostępu Lista ACL dla „%(object)s” wykorzystująca rolę „%(role)s” już istnieje. Zamiast tego edytuj ten wpis ACL. Dostępne uprawnienia Rozdzielona przecinkami lista uprawnień kluczy głównych dla udzielenia dostępu do listy kontroli dostępu. Usuń Usuń listę ACL: %s Wyłączone prawa są dziedziczone z obiektu rodzica lub bezpośrednio nadane dla roli i nie mogą być usunięte w tym widoku. Dziedziczone prawa muszą być usunięte z listy ACL obiektu rodzica lub z roli w menu Ustawień. Edytuj listy ACL Przydziel dostęp dla dokumentu Przyznaj dostęp do obiektu Przyznane uprawnienia Niewystarczający dostęp dla: %s Nowa lista ACL Nowe listy ACL dla: %s Brak uprawnienia: %s Numeryczny identyfikator obiektu, dla którego dostęp zostanie zmodyfikowany. Obiekt "%s" nie jest modelem i nie może być sprawdzony pod kątem dostępu. ID obiektu Typ obiektu Uprawnienia Uprawnienia do nadawania/odwoływania do/z roli dla obiektu. Klucz główny nowego uprawnienia dla udzielenia dostępu do listy kontroli dostępu. Klucze główne roli, z którymi związana jest ta lista kontroli dostępu. Zabierz dostęp do dokumentu Odbierz dostęp do obiektu Rola Uprawnienia roli "%(role)s" dla obiektu "%(object)s" Rola "%(role)s" uprawnienia dla "%(object)s". Role Role, których dostęp zostanie zmodyfikowany. Brak listy ACL dla tego objektu Typ obiektu, dla którego dostęp zostanie zmodyfikowany. Przeglądaj listy ACL 