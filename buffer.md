https://lecturesinparis.onrender.com

/// push to git

cd /Users/edouard.glc/lecturesinparis/lecturesinparis/pvvie25release
source venv/bin/activate
git status
git add .
git commit -m "Your commit message here"
git push origin main
deactivate

////Activate venv
cd /Users/edouard.glc/lecturesinparis/lecturesinparis/pvvie25release
source venv/bin/activate

deactivate

///Extract Prompt

Help me extract the website: 
https://www.bourdelle.paris.fr/visiter/preparer-sa-visite/agenda

Find the html class to target: 
titles like: "Bourdelle et le portrait sculpté : donner vie une seconde fois » - Conférence par Valérie Montalbetti, conservatrice au musée Bourdelle",
date like: "5 juin 2025", 
time like: "",
description like: "Les portraits occupent une part essentielle dans la production sculptée d’Antoine Bourdelle, pour qui le buste constitue un exercice salutaire, stimulant l’imagination et les facultés créatrices. 

Convaincu que chaque visage représente l’infini de la nature, le sculpteur conseille à ses élèves de « faire des bustes ». Mais, comme la vie est mouvante, il estime impossible de saisir un visage, d’en épuiser les formes – tout au plus peut-on en approcher les mystères.

Bourdelle se veut fidèle à la ressemblance physique. Il cherche en outre la vérité du modèle, ce qui rend chacun unique. Il manque encore un élément décisif : il existe entre le sculpteur et son modèle, quelque chose d’impalpable qui demande à être traduit. Enfin, une fois le modèle parfaitement appréhendé, le sculpteur le traduit formellement, pour le transfigurer et l’élever au rang d’œuvre d’art.

Comme l’écrit le poète André Suarès : « Tous les hommes et femmes sculptés par Bourdelle sont cent fois plus eux-mêmes dans le bronze ou la pierre que dans leur enveloppe charnelle ».

De 18h30 à 19h30
Entrée gratuite, sur réservation”,
link like: “https://www.bourdelle.paris.fr/visiter/preparer-sa-visite/agenda/bourdelle-et-le-portrait-sculpte-donner-vie-une-seconde-fois-conference-par-valerie-montalbetti-conservatrice-au-musee-bourdelle”,
location like: "Musée Bourdelle".

Put everything in this way: 
“{
# IRCAM
"url": "https://www.ircam.fr/agenda/tag/rencontres",
"selectors": {
"titles": ".event-line-box__title",
"descriptions": ".event-line-box__desc",
"dates": ".page__meta-date",
"time": "", # Leave empty if not available
"locations": ".page__meta-title",
"links": ".button.mt1.event__meta__btn"
},
"static_location": "" # Leave empty if location is dynamic
}
“

An exerpt of the html is:"
<div class="container">
              
        
            
  <nav class="nav-breadcrumb" aria-label="Fil d’ariane" role="navigation">
    <ol class="breadcrumb">
                                <li>
          <a href="/">Accueil</a>
                </li>
                        <span class="sep" aria-hidden="true">/</span>
                          <li>
          <a href="/visiter">Visiter</a>
                </li>
                        <span class="sep" aria-hidden="true">/</span>
                          <li>
          <a href="/visiter/preparer-sa-visite">Préparer sa visite</a>
                </li>
                        <span class="sep" aria-hidden="true">/</span>
                          <li class="active">
          <a href="" aria-current="true">Agenda</a>
                </li>
          </ol>
  </nav>

    
            <div data-drupal-messages-fallback="" class="hidden"></div>    
        
            
<section class="section section-gray section-header-text mb-5">
  <div class="row">
    <div class="col-md-11 offset-md-1">
      <h1 class="section-title">Agenda</h1>
              <div class="lead">
          <p>Retrouvez notre programmation culturelle : activités, événements et animations pour grands et petits.</p>
        </div>
          </div>
  </div>
          
        
                  <div class="row">
      <div class="col-md-11 offset-md-1">
        <div class="nav-filter">
          <form class="views-exposed-form" data-drupal-selector="views-exposed-form-content-list-agenda" action="/visiter/preparer-sa-visite/agenda" method="get" id="views-exposed-form-content-list-agenda" accept-charset="UTF-8" data-once="exposed-form">
  <div class="form-filter">
  <div class="row">

          <div class="col-sm-4 col-lg-3 mb-3 mb-md-0">
          
<div class="form-group js-form-item form-item js-form-type-date form-type-date js-form-item-date form-item-date form-no-label">
                          <label for="edit-date" class="sr-only">Date :</label>

        <input type="date" data-drupal-selector="edit-date" id="edit-date" name="date" value="" size="30" class="form-date form-control">

        
      <div class="help-block"></div>
</div>

      </div>
              <div class="col-sm-4 col-lg-3 mb-3 mb-md-0">
          
<div class="form-group">
    <label for="edit-category" class="sr-only">Activité :</label>

  
<div class="select">
  <select data-drupal-selector="edit-category" id="edit-category" name="category" class="form-select form-control form-select" autocomplete="off">
                  <option value="All" selected="selected">Activité</option>
                        <option value="5">Atelier</option>
                        <option value="79">Concert</option>
                        <option value="96">Conférence</option>
                        <option value="90">Evénement</option>
                        <option value="6">Lecture</option>
                        <option value="11">Rencontre</option>
                        <option value="12">Spectacle</option>
                        <option value="13">Théâtre</option>
                        <option value="7">Visite</option>
            </select>
  <i class="fas fa-chevron-down" aria-hidden="true"></i>
</div>

  </div>

      </div>
              <div class="col-sm-4 col-lg-3 mb-3 mb-md-0">
          
<div class="form-group">
    <label for="edit-public" class="sr-only">Public :</label>

  
<div class="select">
  <select data-drupal-selector="edit-public" id="edit-public" name="public" class="form-select form-control form-select" autocomplete="off">
                  <option value="All" selected="selected">Public</option>
                        <option value="92">Adultes</option>
                        <option value="8">En famille</option>
                        <option value="85">Enfants</option>
                        <option value="10">Individuels</option>
                        <option value="93">Personnes en situation de handicap</option>
            </select>
  <i class="fas fa-chevron-down" aria-hidden="true"></i>
</div>

  </div>

      </div>
        <div class="col-sm-12 col-lg-3 mt-md-3 mt-lg-0">
      <div>
        <button type="submit" class="button btn btn-primary">Filtrer</button>
        <button type="reset" class="button btn btn-link reset-btn">Réinitialiser</button>

      </div>
    </div>
  </div>
  
  
  <div data-drupal-selector="edit-actions" class="form-actions js-form-wrapper form-wrapper" id="edit-actions"></div>

</div>

</form>

        </div>
      </div>
    </div>
  
    
  </section>

    
        
            
  

<div class="js-view-dom-id-7f63d817905d212fca4acbd9741876fa481beb6070415e3106a709b412058b2f" data-once="ajax-pager">
      


<div class="card card-h">
  <div class="row">
          <div class="col-4 col-md-2 offset-lg-1">
        <h2 class="agenda-title">5 juin<br>2025</h2>
      </div>
        <div class="col-8 col-md-2">
      <div class="card-img img-shadow">
          <img loading="lazy" src="/sites/default/files/styles/196x261/public/2025-02/conference_5_juin_2025.jpg?h=cd2a4617&amp;itok=mNrIiyGj" alt="">



      </div>
    </div>
    <div class="col-12 col-md-6 col-lg-5">
      <div class="card-body d-flex">
        <div>
                      <p class="card-label">Conférence</p>
                    <h3 class="card-title">
                          <a href="/visiter/preparer-sa-visite/agenda/bourdelle-et-le-portrait-sculpte-donner-vie-une-seconde-fois-conference-par-valerie-montalbetti-conservatrice-au-musee-bourdelle">« Bourdelle et le portrait sculpté : donner vie une seconde fois » - Conférence par Valérie Montalbetti, conservatrice au musée Bourdelle</a>
                      </h3>
          <p class="text-align-justify"><span>Les portraits occupent une part essentielle dans la production sculptée d’Antoine Bourdelle, pour qui le buste constitue un exercice salutaire, stimulant l’imagination et les facultés créatrices.&nbsp;</span></p><p class="text-align-justify"><span>Convaincu que chaque visage représente l’infini de la nature, le sculpteur conseille à ses élèves de « faire des bustes ». Mais, comme la vie est mouvante, il estime impossible de saisir un visage, d’en épuiser les formes – tout au plus peut-on en approcher les mystères.</span></p><p class="text-align-justify"><span>Bourdelle se veut fidèle à la ressemblance physique. Il cherche en outre la vérité du modèle, ce qui rend chacun unique. Il manque encore un élément décisif : il existe entre le sculpteur et son modèle, quelque chose d’impalpable qui demande à être traduit. Enfin, une fois le modèle parfaitement appréhendé, le sculpteur le traduit formellement, pour le transfigurer et l’élever au rang d’œuvre d’art.</span></p><p class="text-align-justify"><span>Comme l’écrit le poète André Suarès : « Tous les hommes et femmes sculptés par Bourdelle sont cent fois plus eux-mêmes dans le bronze ou la pierre que dans leur enveloppe charnelle ».</span></p>
                    <p class="card-text mt-4 mb-4">
            De 18h30 à 19h30<br>
                          Entrée gratuite, sur réservation
                        </p>
          <p class="card-text">Adultes • Individuels</p>
        </div>
      </div>
    </div>

    <div class="col-12 col-md-2 text-end">
      

  <p>
          <a href="https://www.billetterie-parismusees.paris.fr/selection/timeslotpass?productId=10229345784028" class="btn btn-primary btn-sm-full" target="_blank">Réservez une place</a>
      </p>

    </div>
  </div>
</div>

    




  </div>





    


    

        
        
                  <hr>
    <h2 class="h1">Pour aller plus loin</h2>
    <div class="row"><div class="col-md-4">
      

<div class="card">
    <div class="card-img">
          <img loading="lazy" src="/sites/default/files/styles/416x312/public/2024-05/pa23_musee_bourdelle_2051_hd.jpg?h=f0ab467d&amp;itok=3Ew2dGpM" alt="Le mur des moulages, dans l'atelier de sculpture du musée Bourdelle">



    </div>

    <div class="card-body">
        <div>
                                        <h3 class="card-title">
                  <a href="/visiter/preparer-sa-visite/informations-pratiques">Informations pratiques</a></h3>
                                                        </div>
    </div>
</div>

    </div><div class="col-md-4">
      

<div class="card">
    <div class="card-img">
          <img loading="lazy" src="/sites/default/files/styles/416x312/public/2024-06/009_musre_bourdelle_bfjuin2015.jpg?h=ab8aab16&amp;itok=ZX6SSSJy" alt="Vue des façades d'ateliers donnant sur le jardin intérieur">



    </div>

    <div class="card-body">
        <div>
                                        <h3 class="card-title">
                  <a href="/decouvrir/le-musee/actualites">Actualités</a></h3>
                                                        </div>
    </div>
</div>

    </div><div class="col-md-4">
      

<div class="card">
    <div class="card-img">
          <img loading="lazy" src="/sites/default/files/styles/416x312/public/2024-06/visuel_bmo_newsletter_pm__0.jpg?h=96f233f8&amp;itok=qjMHGMcT" alt="Visuel de l'accrochage La mémoire des objets">



    </div>

    <div class="card-body">
        <div>
                                        <h3 class="card-title">
                  <a href="/visiter/expositions/expositions-en-cours">Expositions en cours</a></h3>
                                                        </div>
    </div>
</div>

    </div></div>

  
    
    
<div class="card card-h card-primary mt-6 mb-6">
  <div class="row">
    <div class="col-sm-6 offset-sm-1 order-2 position-relative">
      <div class="card-img img-right">
        
  <img loading="lazy" src="/sites/default/files/styles/416x306/public/2024-06/img_3354_2.jpg?h=6f8e8448&amp;itok=tGpdeYPa" alt="">




      </div>
    </div>
    <div class="col-sm-5 order-1 d-flex align-items-center">
      <div class="card-body d-flex">
        <div>
                                <h2 class="card-title-2 mb-1">Suivez l’actualité du musée Bourdelle </h2>
                                <p class="card-lead">
              Abonnez-vous à notre newsletter
            </p>
                    
                  </div>

                  <p class="mb-0 mt-4">
            <a class="btn btn-primary" href="/sinscrire-notre-lettre-dinformation">Je m’abonne</a>
          </p>
              </div>
    </div>
  </div>
</div>

  </div>
"








////////////////////////////////////////////////////////////////////////////////////////////
///Extract Prompt (individual pages)

Help me extract the website: 
https://iicparigi.esteri.it/fr/gli_eventi/calendario/concert-francesco-turrini-piano-solo/

Find the html class to target: 
date like: "mai 22 2025, 19:00 (Heure locale)", 
time like: "mai 22 2025, 19:00 (Heure locale)",
description like: "Le pianiste Francesco Turrisi, l’un des rares Italiens à avoir remporté un Grammy Award, a été qualifié d’« alchimiste » et de « polyglotte musical » par la presse internationale. Northern Migrations, son dernier album pour piano solo, « délicat, mélancolique et fascinant » selon The Irish Times, a été présenté en Irlande, en France, en Allemagne, en Italie, aux États-Unis et en Nouvelle-Zélande, et débarque aujourd’hui pour la première fois à la Casa del Jazz de Rome.
Francesco fait partie du célèbre ensemble de musique ancienne l’Arpeggiata avec lequel il s’est produit dans les plus grands festivals et théâtres du monde, du Carnegie Hall de New York au Queen Elisabeth Hall de Londres, enregistrant pour de grands labels tels que Warner, Virgin, Naive et Alpha. Depuis 2018, Francesco collabore avec la célèbre chanteuse et multi-instrumentiste américaine Rhiannon Giddens. En 2019, le single I’m on my way a reçu une nomination aux GRAMMY awards tandis que le deuxième album, They’re calling me home, sorti sur le label Nonesuch, a reçu deux nominations aux Grammy Awards et a remporté un Grammy Award en 2022 dans la catégorie Meilleur album folk.
Francesco est aussi à l’aise pour improviser avec des vétérans du jazz comme Dave Liebman et Bill Frisell que pour accompagner la chanteuse traditionnelle irlandaise Roisin El Safty ou la chanteuse traditionnelle italienne Lucilla Galeazzi. Il a fait une tournée avec Bobby McFerrin, a interprété la musique de Steve Reich avec les Bang on a Can All Stars, a accompagné la star du flamenco Pepe El Habichuela et a joué en duo avec la chanteuse grecque Savina Yannatou. Il a collaboré avec Bobby McFerrin, Dave Liebman, Gianluigi Trovesi, Christian McBride, Yo Yo Ma, Bill Frisell, Rhiannon Giddens, Nils Landgren, Wolfgang Muthspiel, Gabriele Mirabassi, Rolando Villazon, Lisa Hannigan, Savina Yannatou, Maria Pia de Vito, Theodosii Spassov, The King’s Singers, Veronique Gens, Philippe Jaroussky, Pepe el Habichuela, Lucilla Galeazzi. « Sa capacité à réarranger des mélodies et des rythmes anciens à travers le prisme du jazz contemporain fait de lui l’un des musiciens les plus impressionnants à avoir émergé de la scène européenne du jazz au cours de la dernière décennie », All About Jazz

En collaboration avec le Centre culturel irlandais.

”,


Put everything in this way under the individual_page_selectors : 
“{
        # Example website
        "url": "https://example.com/events",
        "selectors": {
            "titles": ".event-title",
            "descriptions": ".event-description",  # For the main page
            "dates": ".event-date",
            "time": ".event-time",
            "locations": ".event-location",
            "links": ".event-link"
        },
        "individual_page_selectors": {
            "descriptions": ".individual-description",  # For the individual event page
            "dates": ".individual-date",
            "time": ".individual-time"
        },
        "static_location": "Example Location",
        "pagination": None
    }
“

An exerpt of the html is:"<div class="col-lg-8">
					<!-- Breadcrumbs e social sharing -->
					<div class="row">
						<div class="col-lg-8">
							<nav class="breadcrumb-container" aria-label="breadcrumb"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="https://iicparigi.esteri.it/fr/">Page d'accueil</a><span class="separator">&gt;</span></li><li class="breadcrumb-item"></li><li class="breadcrumb-item">
                            <a href="https://iicparigi.esteri.it/fr/gli_eventi/">Événements</a></li><li class="breadcrumb-item"><span class="separator">&gt;</span></li><li class="breadcrumb-item">
                            <a href="https://iicparigi.esteri.it/fr/gli_eventi/calendario/">Événements programmés</a></li><li class="breadcrumb-item"><span class="separator">&gt;</span></li><li class="breadcrumb-item active" aria-current="page">Concert / Francesco Turrisi piano solo</li></ol></nav>						</div>
						<div class="col-lg-4">
							
    <!-- Share button -->
    <div class="share_buttons reveal-content clearfix">
        <div class="share_buttons_container float-start clearfix pe-2">
            <a href="https://www.facebook.com/sharer/sharer.php?u=https://iicparigi.esteri.it/fr/concert-francesco-turrini-piano-solo/" title="Partager sur Facebook">
                <svg class="icon icon-lg icon-padded bg-primary icon-white">
                    <use xlink:href="https://iicparigi.esteri.it/wp-content/themes/sedi-tema/assets/svg/sprites.svg#it-facebook"></use>
                </svg>
                <span class="visually-hidden">Partager sur Facebook</span>
            </a>
            <a href="https://twitter.com/intent/tweet?url=https://iicparigi.esteri.it/fr/concert-francesco-turrini-piano-solo/" title="Partager sur Twitter">
                <svg class="icon icon-lg icon-padded bg-primary icon-white">
                    <use xlink:href="https://iicparigi.esteri.it/wp-content/themes/sedi-tema/assets/svg/sprites.svg#it-twitter"></use>
                </svg>
                <span class="visually-hidden">Partager sur Twitter</span>
            </a>
            <a href="https://api.whatsapp.com/send?text=https://iicparigi.esteri.it/fr/concert-francesco-turrini-piano-solo/" data-action="share/whatsapp/share" title="Partager sur WhatsApp">
                <svg class="icon icon-lg icon-padded bg-primary icon-white">
                    <use xlink:href="https://iicparigi.esteri.it/wp-content/themes/sedi-tema/assets/svg/sprites.svg#it-whatsapp"></use>
                </svg>
                <span class="visually-hidden">Partager sur WhatsApp</span>
            </a>
        </div>
        <!-- /share_buttons_container -->
        <span class="bg-light share-span">Partager</span>
            <a href="#" onclick="return false" title="Partager sur les réseaux sociaux" class="share_buttons_trigger reveal-trigger">
                <svg class="icon icon-lg icon-padded bg-primary icon-white align-middle">
                  <use xlink:href="https://iicparigi.esteri.it/wp-content/themes/sedi-tema/assets/svg/sprites.svg#it-share"></use>
                </svg>
                <span class="visually-hidden">Partager sur les réseaux sociaux</span>
            </a>
    </div>						</div>
					</div>
		
<article id="post-12153" class="post-12153 eventi type-eventi status-publish has-post-thumbnail hentry">
	
	<header class="entry-header">
		<h1 class="entry-title h3">Concert / Francesco Turrisi piano solo</h1>	</header><!-- .entry-header -->

		    <figure>
            <img width="849" height="526" src="https://iicparigi.esteri.it/wp-content/uploads/2025/02/FrancescoTurrisi_2018-1.jpg" srcset="https://iicparigi.esteri.it/wp-content/uploads/2025/02/FrancescoTurrisi_2018-1.jpg 849w, https://iicparigi.esteri.it/wp-content/uploads/2025/02/FrancescoTurrisi_2018-1-300x186.jpg 300w, https://iicparigi.esteri.it/wp-content/uploads/2025/02/FrancescoTurrisi_2018-1-768x476.jpg 768w" sizes="(max-width: 849px) 100vw, 849px" class="img-fluid" alt="FrancescoTurrisi_2018">
                <figcaption class="figure-caption visually-hidden"></figcaption>
        </figure>

		
		<div class="entry-meta">
					<ul class="list-inline">
			 
            <li class="list-inline-item">
				<svg class="icon icon-primary icon-sm">
					<use xlink:href="https://iicparigi.esteri.it/wp-content/themes/sedi-tema/assets/svg/sprites.svg#it-calendar"></use>
				</svg>
				<small><b>Date de l'événement:</b> La mai 22 2025, 19:00 (Heure locale)</small>
			</li>
									 
            <li class="list-inline-item">
				<svg class="icon icon-primary icon-sm">
					<use xlink:href="https://iicparigi.esteri.it/wp-content/themes/sedi-tema/assets/svg/sprites.svg#it-info-circle "></use>
				</svg>
				<small><b>Pour un coût supplémentaire:</b> Non</small>
			</li>
			        </ul>
				</div><!-- .entry-meta -->

	<div class="entry-content">
		<p>Le pianiste <strong>Francesco Turrisi</strong>, l’un des rares Italiens à avoir remporté un Grammy Award, a été qualifié d’« alchimiste » et de « polyglotte musical » par la presse internationale. Northern Migrations, son dernier album pour piano solo, « délicat, mélancolique et fascinant » selon The Irish Times, a été présenté en Irlande, en France, en Allemagne, en Italie, aux États-Unis et en Nouvelle-Zélande, et débarque aujourd’hui pour la première fois à la Casa del Jazz de Rome.<br>
Francesco fait partie du célèbre ensemble de musique ancienne l’Arpeggiata avec lequel il s’est produit dans les plus grands festivals et théâtres du monde, du Carnegie Hall de New York au Queen Elisabeth Hall de Londres, enregistrant pour de grands labels tels que Warner, Virgin, Naive et Alpha. Depuis 2018, Francesco collabore avec la célèbre chanteuse et multi-instrumentiste américaine Rhiannon Giddens. En 2019, le single I’m on my way a reçu une nomination aux GRAMMY awards tandis que le deuxième album, They’re calling me home, sorti sur le label Nonesuch, a reçu deux nominations aux Grammy Awards et a remporté un Grammy Award en 2022 dans la catégorie Meilleur album folk.<br>
Francesco est aussi à l’aise pour improviser avec des vétérans du jazz comme Dave Liebman et Bill Frisell que pour accompagner la chanteuse traditionnelle irlandaise Roisin El Safty ou la chanteuse traditionnelle italienne Lucilla Galeazzi. Il a fait une tournée avec Bobby McFerrin, a interprété la musique de Steve Reich avec les Bang on a Can All Stars, a accompagné la star du flamenco Pepe El Habichuela et a joué en duo avec la chanteuse grecque Savina Yannatou. Il a collaboré avec Bobby McFerrin, Dave Liebman, Gianluigi Trovesi, Christian McBride, Yo Yo Ma, Bill Frisell, Rhiannon Giddens, Nils Landgren, Wolfgang Muthspiel, Gabriele Mirabassi, Rolando Villazon, Lisa Hannigan, Savina Yannatou, Maria Pia de Vito, Theodosii Spassov, The King’s Singers, Veronique Gens, Philippe Jaroussky, Pepe el Habichuela, Lucilla Galeazzi. « Sa capacité à réarranger des mélodies et des rythmes anciens à travers le prisme du jazz contemporain fait de lui l’un des musiciens les plus impressionnants à avoir émergé de la scène européenne du jazz au cours de la dernière décennie », All About Jazz</p>
<p>En collaboration avec le Centre culturel irlandais.</p>
<p><a href="https://my.weezevent.com/concert-francesco-turrisi-piano-solo?_gl=1*137qbbx*_gcl_au*Nzc4MTc3NTYuMTczNDQ1MjcxMi41ODkzOTgxOTcuMTczOTUzNTgyNC4xNzM5NTM3NTAw*_ga*MTk5NDI4OTM1MS4xNzAwNjY4Njkw*_ga_39H9VBFX7G*MTczOTUzNDk0NC40MTMuMS4xNzM5NTM4NTY4LjYwLjAuMTg1MzYyMzMzMA..">Reservez vos places ici.</a></p>
	</div><!-- .entry-content -->

	<footer class="entry-footer">
			</footer><!-- .entry-footer -->
</article><!-- #post-12153 -->
			</div>
"