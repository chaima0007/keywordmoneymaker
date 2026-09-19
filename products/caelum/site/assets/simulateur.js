/* Caelum — logique du simulateur « Suis-je concerné ? ».
   Fichier externe (conforme CSP script-src 'self'). Logique inchangée :
   tout se calcule dans le navigateur, aucune donnée n'est envoyée.
   Faits légaux datés et sourcés — voir commentaires. */
(function () {
  "use strict";
  var form = document.getElementById("simu");
  if (!form) return;

  // Progression visuelle (facultative) : met à jour les segments quand on répond.
  var prog = document.querySelectorAll(".progress span");
  if (prog.length) {
    form.addEventListener("change", function () {
      var noms = ["q1", "q2", "q3", "q4"], n = 0;
      noms.forEach(function (nm) { if (form.querySelector('input[name="' + nm + '"]:checked')) n++; });
      for (var i = 0; i < prog.length; i++) prog[i].classList.toggle("on", i < n);
    });
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var v = function (n) {
      var el = form.querySelector('input[name="' + n + '"]:checked');
      return el ? el.value : null;
    };
    var q1 = v("q1"), q2 = v("q2"), q3 = v("q3"), q4 = v("q4");
    if (!q1 || !q2 || !q3 || !q4) {
      alert("Merci de répondre aux 4 questions.");
      return;
    }
    var res = [];
    // E-facturation — fait vérifié : obligatoire depuis le 01/01/2026 (Peppol), assujettis TVA établis en Belgique, B2B.
    if (q1 === "oui") {
      res.push({ n: "E-facturation B2B (Peppol)", s: "oui",
        t: "Applicable. Obligatoire depuis le 01/01/2026 pour les factures entre assujettis TVA établis en Belgique — le régime de la franchise compris. Vérifiez que votre logiciel émet ET reçoit via Peppol : un PDF par e-mail ne suffit plus. Quatre situations en dispensent : ne réaliser que des opérations exemptées par l'article 44 du Code TVA, relever du régime forfaitaire (article 56, jusqu'au 01/01/2028 au plus tard), être en faillite, ou être identifié à la TVA en Belgique sans y être établi. Prochaine échéance connue : e-reporting prévu pour 2028." });
    } else if (q1 === "nsp") {
      res.push({ n: "E-facturation B2B (Peppol)", s: "verifier",
        t: "À vérifier. Si votre entreprise est assujettie à la TVA en Belgique et facture d'autres entreprises, l'obligation s'applique depuis le 01/01/2026. Votre comptable peut le confirmer en quelques minutes." });
    } else {
      res.push({ n: "E-facturation B2B (Peppol)", s: "verifier",
        t: "Vos factures sortantes ne sont pas concernées : celles adressées à des particuliers échappent à l'obligation. Mais attention à la moitié qu'on oublie — si vous avez un numéro de TVA belge, vous devez être en mesure de RECEVOIR les factures électroniques structurées de vos fournisseurs. C'est le seul point à régler de votre côté. Source : efacture.belgium.be." });
    }
    // NIS2 — loi 26/04/2024, en vigueur 18/10/2024 ; secteurs + taille ; échéance essentielles 18/04/2026.
    if (q3 === "oui" && q2 === "plus50") {
      res.push({ n: "NIS2 (cybersécurité)", s: "oui",
        t: "Probablement applicable : secteur visé et 50 travailleurs ou plus. La loi belge du 26/04/2024 est en vigueur depuis le 18/10/2024 ; l'échéance du 18/04/2026 pour les entités essentielles est passée. Vérifiez votre statut exact (essentielle ou importante) sur ccb.belgium.be — c'est la source officielle." });
    } else if (q3 === "oui" || q3 === "nsp") {
      res.push({ n: "NIS2 (cybersécurité)", s: "verifier",
        t: "À vérifier. NIS2 dépend du secteur ET de critères de taille (souvent 50 salariés et plus, avec des exceptions selon le secteur). Consultez la liste officielle du Centre pour la Cybersécurité Belgique (ccb.belgium.be) — beaucoup d'entreprises découvrent qu'elles ne sont PAS concernées." });
    } else {
      res.push({ n: "NIS2 (cybersécurité)", s: "non",
        t: "A priori non applicable : votre secteur n'est pas dans la liste. C'est une bonne nouvelle à documenter — savoir pourquoi on n'est pas concerné est aussi une preuve de sérieux face à vos clients." });
    }
    // RGPD — toutes entreprises traitant des données personnelles.
    if (q4 === "oui") {
      res.push({ n: "RGPD (données personnelles)", s: "oui",
        t: "Applicable — comme pour toute entreprise qui traite des données personnelles, quelle que soit sa taille. Les trois chantiers concrets : savoir quelles données vous détenez et où, documenter pourquoi et combien de temps vous les gardez, encadrer vos sous-traitants. Source officielle : autoriteprotectiondonnees.be." });
    } else {
      res.push({ n: "RGPD (données personnelles)", s: "verifier",
        t: "Sur la base de votre réponse, le RGPD ne s'appliquerait pas. C'est possible, mais rare : une boîte mail professionnelle, un carnet d'adresses ou un seul bulletin de paie suffisent à faire de vous un responsable de traitement — et dans ce cas il s'applique, quelle que soit votre taille." });
    }
    // Lanceurs d'alerte — loi 28/11/2022, ≥50 travailleurs.
    if (q2 === "plus50") {
      res.push({ n: "Canal lanceurs d'alerte", s: "oui",
        t: "Applicable : la loi du 28/11/2022 impose un canal de signalement interne confidentiel aux entreprises d'au moins 50 travailleurs. Vérifiez qu'un dispositif existe et que vos travailleurs le connaissent." });
    } else {
      // Verdict « à vérifier » et non « non concerné » : ce questionnaire ne demande PAS
      // si vous relevez du secteur financier ou de l'anti-blanchiment, où la loi s'applique
      // sans aucun seuil d'effectif. Rendre « a priori non concerné » à une fiduciaire de
      // douze personnes serait une affirmation de droit fausse. Le §14 du protocole tranche :
      // quand les faits ne départagent pas, le verdict le plus prudent gagne.
      res.push({ n: "Canal lanceurs d'alerte", s: "verifier",
        t: "À vérifier. En règle générale l'obligation commence à 50 travailleurs — mais elle s'applique SANS SEUIL, quel que soit votre effectif, si vous relevez des dispositions en matière de services, produits et marchés financiers, ou si vous êtes assujetti à la législation anti-blanchiment. Beaucoup de petites structures le sont sans le savoir. Ce test ne vous pose pas la question : vérifiez votre situation. Si aucune des deux ne vous concerne, l'obligation ne commence qu'à 50 travailleurs." });
    }
    // CSRD / DORA — démystification honnête, toujours affichée.
    // « à vérifier » et non « non concerné » : ce questionnaire ne mesure NI le chiffre
    // d'affaires NI le total de bilan. Tant que l'Omnibus n'est pas transposé, ce sont
    // les seuils nettement plus bas de la loi du 02/12/2024 qui s'appliquent — une
    // société belge peut donc être concernée AUJOURD'HUI et lire « non concerné ».
    res.push({ n: "CSRD et DORA — le point honnête", s: "verifier",
      t: "CSRD : le paquet Omnibus du 24/02/2026 (directive (UE) 2026/470) relève fortement les seuils — il faudra dépasser À LA FOIS 1 000 salariés ET 450 M€ de chiffre d'affaires net. Cette directive n'est pas encore transposée en droit belge : jusque-là, ce sont les seuils, nettement plus bas, de la loi du 02/12/2024 qui s'appliquent. Ce test ne mesure ni votre chiffre d'affaires ni votre total de bilan : il ne peut donc pas trancher à votre place. La grande majorité des PME n'est pas concernée ; si vous êtes une grande société au sens du Code des sociétés et des associations, vérifiez avec votre réviseur. DORA : secteur financier et prestataires TIC uniquement. Si on vous vend l'un ou l'autre comme une urgence PME, demandez la source." });

    var lib = { oui: "S'applique à vous", verifier: "À vérifier", non: "A priori non concerné" };
    var cont = document.getElementById("res-liste");
    cont.innerHTML = "";
    res.forEach(function (r) {
      var d = document.createElement("div");
      d.className = "res-carte res-" + r.s;
      d.innerHTML = '<span class="etiquette">' + lib[r.s] + "</span><h3>" + r.n + "</h3><p>" + r.t + "</p>";
      cont.appendChild(d);
    });

    var corps = "Bonjour,%0D%0A%0D%0AVoici mon résultat au simulateur Caelum :%0D%0A" +
      res.map(function (r) { return "- " + r.n + " : " + lib[r.s]; }).join("%0D%0A") +
      "%0D%0A%0D%0AJe souhaite recevoir la synthèse écrite et être informé(e) de vos outils de conformité (consentement donné par cet envoi, désinscription sur simple demande).%0D%0A%0D%0ANom de l'entreprise : %0D%0ASecteur : ";
    document.getElementById("mail-resultat").setAttribute("href",
      "mailto:chaima.caelumpartners@gmail.com?subject=" + encodeURIComponent("Mon résultat — simulateur Caelum") + "&body=" + corps);

    var sec = document.getElementById("resultat");
    sec.hidden = false;
    sec.scrollIntoView({ behavior: "smooth", block: "start" });
  });
})();
