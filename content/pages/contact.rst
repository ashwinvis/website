Contact
#######
:date: 2019-10-18
:slug: contact
:status: published
:html_header:
   <script language="JavaScript" type="text/javascript">
   \  function decrypt_email(a) {
   \    // ROT13 : a Caesar cipher
   \    // letter -> letter' such that code(letter') = (code(letter) + 13) modulo 26
   \    return a.replace(/[a-zA-Z]/g,
   \                     function(c){
   \             return String.fromCharCode((c <= "Z" ? 90 : 122) >= (c = c.charCodeAt(0) + 13) ? c : c - 26);
   \         })
   \  }
   \  // Generated using src/util.py
   \  function openPersonalMail(element) {
   \    var y = decrypt_email("znvygb:Nfujva Ivfuah Zbunana <nfujvaivf@cz.zr>");
   \    element.setAttribute("href", y);
   \  }
   \  function openWorkMail(element) {
   \    var y = decrypt_email("znvygb:Nfujva Zbunana <nfujva.zbunana@fzuv.fr>");
   \    element.setAttribute("href", y);
   \  }
   \ </script>
   \  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.8.0/dist/leaflet.css"
   \    integrity="sha512-hoalWLoI8r4UszCkZ5kL8vayOGVae1oxXe/2A4AO6J9+580uKHDO3JdHb7NzwwzK5xr/Fs0W40kiNHxM9vyTtQ=="
   \    crossorigin=""/>
   \ <script src="https://unpkg.com/leaflet@1.8.0/dist/leaflet.js"
   \    integrity="sha512-BB3hKbKWOc9Ez/TAwyWxNXeoV9c1v6FIeYiBieIWkpLjauysF18NzgR1MBNBXf8/KABdlkX68nAhlwcDFLGPCQ=="
   \    crossorigin=""></script>
   \ <script language="JavaScript" type="text/javascript">
   \    var map = L.map('map').setView([58.581188, 16.148062], 13);
   \    var marker = L.marker([58.581188, 16.148062]).addTo(map);
   \ </script>

I would love to hear from you!
Drop me a message if you wish to talk to me or even leave a comment about my
research_ or software_ that I maintain.

.. raw:: html

   <table class="m-table m-flat m-big">
   <tbody>
     <tr>
       <td class="m-text-center">
         <div class="m-button m-info m-fullwidth" align-content="normal">
                   <div class="m-big"><b>Visiting / mailing address</b></div>
                   <span class="m-text m-small">
                       Folkborgsvägen 17, SE-601 76<br/>
                       Norrköping, Sweden
                   </span>
         </div>
       </td>
     </tr>

     <tr>
     <td>
       <div class="m-button m-flat m-fullwidth">
         <a href="encrypted-personal-mail:Click to reveal" onclick="openPersonalMail(this);">
             <div class="m-big">Personal e-mail</div>
             <div class="m-small">Click to mail</div>
         </a>
       </div>
     </td>
     <td>
       <div class="m-button m-flat m-fullwidth">
         <a href="encrypted-work-mail:Click to reveal" onclick="openWorkMail(this);">
             <div class="m-big">Work e-mail</div>
             <div class="m-small">Click to mail</div>
         </a>
       </div>
     </td>
     </tr>

     </tbody>
     </table>

.. block-info:: Find directions to my office

    I try to be at the university once a week, despite working from home most
    of the time. Let me know beforehand if you drop by.

    .. container:: m-row

        .. container:: m-col-l-10 m-push-l-1 m-col-m-7 m-nopadb

            .. raw:: html

                 <style>#map { height: 180px; }</style>
                 <div id="map"></div>


You can also reach me via social media accounts listed in the footer.

.. _research: /pages/research
.. _software: /pages/software