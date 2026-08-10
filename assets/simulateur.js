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
        t: "Applicable. Obligatoire depuis le 01/01/2026 pour les factures entre assujettis TVA établis en Belgique. Vérifiez que votre logiciel émet ET reçoit via Peppol — un PDF par e-mail ne suffit plus. Prochaine échéance connue : e-reporting prévu pour 2028." });
    } else if (q1 === "nsp") {
      res.push({ n: "E-facturation B2B (Peppol)", s: "verifier",
        t: "À vérifier. Si votre entreprise est assujettie à la TVA en Belgique et facture d'autres entreprises, l'obligation s'applique depuis le 01/01/2026. Votre comptable peut le confirmer en quelques minutes." });
    } else {
      res.push({ n: "E-facturation B2B (Peppol)", s: "non",
        t: "A priori non applicable à ce jour sur la base de votre réponse (pas de facturation B2B entre assujettis TVA belges). Si votre situation change, la question se reposera." });
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
        t: "Réponse rare : la quasi-totalité des entreprises traite des données personnelles (une boîte mail professionnelle ou des fiches de paie suffisent). Revérifiez — si vous en traitez, le RGPD s'applique." });
    }
    // Lanceurs d'alerte — loi 28/11/2022, ≥50 travailleurs.
    if (q2 === "plus50") {
      res.push({ n: "Canal lanceurs d'alerte", s: "oui",
        t: "Applicable : la loi du 28/11/2022 impose un canal de signalement interne confidentiel aux entreprises d'au moins 50 travailleurs. Vérifiez qu'un dispositif existe et que vos travailleurs le connaissent." });
    } else {
      res.push({ n: "Canal lanceurs d'alerte", s: "non",
        t: "Non applicable à ce jour : l'obligation commence à 50 travailleurs. À revoir si vous approchez ce seuil." });
    }
    // CSRD / DORA — démystification honnête, toujours affichée.
    res.push({ n: "CSRD et DORA — le point honnête", s: "non",
      t: "CSRD : depuis le paquet Omnibus adopté le 24/02/2026, les seuils ont été fortement relevés (cible ~1 000 salariés) — la grande majorité des PME n'est pas concernée à court terme. DORA : secteur financier et prestataires TIC uniquement. Si on vous vend l'un ou l'autre comme une urgence PME, demandez la source." });

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
