(() => {
  'use strict';
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));
  const data = window.GOLDOURS_DATA || {};
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const safe = (s) => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const query = new URLSearchParams(window.location.search);
  const imgPrefix = 'assets/images/';

  const nav = $('#nav');
  const toggle = $('.menu-toggle');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = !nav.classList.contains('open');
      nav.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.innerHTML = `<i class="fas ${open ? 'fa-times' : 'fa-bars'}" aria-hidden="true"></i>`;
    });
    $$('.nav-drop-trigger').forEach(btn => {
      btn.addEventListener('click', () => {
        const open = btn.getAttribute('aria-expanded') !== 'true';
        $$('.nav-drop-trigger').forEach(other => other.setAttribute('aria-expanded', 'false'));
        btn.setAttribute('aria-expanded', String(open));
      });
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') {
        nav.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false');
        $$('.nav-drop-trigger').forEach(el => el.setAttribute('aria-expanded', 'false'));
      }
    });
  }

  if ('IntersectionObserver' in window && !reduced) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {entry.target.classList.add('visible'); observer.unobserve(entry.target);}
      });
    }, {threshold: .04, rootMargin: '0px 0px 35px 0px'});
    $$('.fade-up').forEach(el => observer.observe(el));
  } else { $$('.fade-up').forEach(el => el.classList.add('visible')); }

  const goTop = $('.back-to-top');
  if (goTop) {
    const refresh = () => goTop.classList.toggle('visible', window.scrollY > 550);
    window.addEventListener('scroll', refresh, {passive:true}); refresh();
    goTop.addEventListener('click', () => window.scrollTo({top:0, behavior:reduced?'instant':'smooth'}));
  }
  $$('.copyright-year').forEach(el => el.textContent = String(new Date().getFullYear()));

  const cookie = $('.cookie-banner');
  if (cookie) {
    let saved = false;
    try { saved = localStorage.getItem('goldours-cookie-consent') === 'accepted'; } catch (err) {}
    cookie.hidden = saved;
    $('#accept-cookies')?.addEventListener('click', () => {
      try {localStorage.setItem('goldours-cookie-consent','accepted');} catch(err) {}
      cookie.hidden = true;
    });
  }

  if (document.body.classList.contains('blog-index')) {
    const cards = $('.blog-card', $('#blog-list'));
    const searchInput = $('#blog-search');
    let active = 'all';
    const run = () => {
      const text = (searchInput.value || '').trim().toLowerCase();
      let found = 0;
      cards.forEach(card => {
        const category = $('.meta span', card)?.textContent.trim() || '';
        const matches = (active === 'all' || category === active) && card.textContent.toLowerCase().includes(text);
        card.hidden = !matches;
        if (matches) found++;
      });
      $('.empty-results').hidden = found !== 0;
      $('.blog-count').textContent = `Showing ${found} of ${cards.length} GoldOurs insights`;
    };
    searchInput?.addEventListener('input', run);
    $('.filter-chip').forEach(btn => btn.addEventListener('click', () => {
      active = btn.dataset.filter;
      $('.filter-chip').forEach(b => b.classList.toggle('active', b === btn));
      run();
    }));
    run();
  }


  if (document.body.classList.contains('blog-detail-page') && Array.isArray(data.articles)) {
    const article = data.articles.find(a => a.id === query.get('article')) || data.articles[0];
    if (article) {
      document.title = `${article.title} | GoldOurs`;
      $('#article-image').src = article.image;
      $('#article-image').alt = article.title;
      $('#article-meta').textContent = `${article.category} · ${article.date} · GoldOurs Insights`;
      $('#article-title').textContent = article.title;
      $('#article-excerpt').textContent = article.description;
      const body = [
        ['Why this matters', `${article.description} For organisations seeking sustainable progress, this is an invitation to examine how leadership choices, information and everyday systems connect to measurable outcomes.`],
        ['From intention to action', 'The most useful starting point is a clear understanding of the current challenge, the decisions it requires and who is accountable for the next step. A practical approach connects strategic direction with responsibilities, resources, timeframes and evidence of progress.'],
        ['Questions worth asking', 'What is happening today? What should success look like? Which priorities deserve attention? How will leaders know whether the organisation is moving in the right direction? Honest answers create the basis for better decisions and lasting improvement.'],
        ['Building a sustainable response', 'GoldOurs encourages organisations to combine thoughtful governance with leadership development, reliable systems and meaningful accountability. The objective is not more activity for its own sake, but greater clarity and more effective execution.']
      ];
      
    }
    $('#copy-article-link')?.addEventListener('click', async e => {
      try {await navigator.clipboard.writeText(location.href); e.currentTarget.textContent = 'Link copied';}
      catch(err) {e.currentTarget.textContent = 'Select URL to copy';}
    });
  }

  if (document.body.classList.contains('media-detail-page') && Array.isArray(data.media)) {
    const n = Math.max(0, Math.min(data.media.length-1, Number(query.get('media') || 0)));
    const item = data.media[n];
    if (item) {
      $('#media-detail-title').textContent = item.title;
      $('#media-detail-category').textContent = item.category;
      $('#media-detail-image').src = item.image;
      $('#media-detail-image').alt = item.title;
    }
  }
  $('#contact-form')?.addEventListener('submit', e => {
    e.preventDefault();
    const form = e.currentTarget;
    if (!form.reportValidity()) return;
    const values = new FormData(form);
    const subject = 'GoldOurs enquiry — ' + (values.get('topic') || 'General enquiry');
    form.subject = subject
    form.submit()
    
    const status = $('.form-message', form);
    if (status) status.textContent = 'Your email application will open with the enquiry ready to send. If it does not open, email info@goldours.co.za directly.';
    
  });

  const profileQuotes = [{"service": "Governance & Direction", "quote": "GoldOurs is competent and their impact is invaluable", "role": "Chief Audit Executive", "org": "CEF SOC Ltd"}, {"service": "Governance & Direction", "quote": "We highly recommend GoldOurs for strategy facilitation because they ensured that our needs were understood and delivered high quality work", "role": "CEO", "org": "Massive Quantum (Pty) Ltd"}, {"service": "Talent Management & Development", "quote": "We recommend GoldOurs because the training facilitator was experienced, knowledgeable and customised the training to our context and training needs", "role": "Senior Manager (Learning & Development)", "org": "Auditor-General of South Africa"}, {"service": "Talent Management & Development", "quote": "The facilitator received great reviews from the participants, especially in relation to making the topics interesting and practical", "role": "Co-ordinator (Learning and Teaching)", "org": "SACAP"}, {"service": "Accounting, Tax & Assurance", "quote": "We are happy to say that GoldOurs contributed positively to our clean audit outcome", "role": "Director", "org": "National Department of Tourism"}, {"service": "Accounting, Tax & Assurance", "quote": "GoldOurs is competent and professional; they contributed to our clean audit outcome", "role": "Chief Audit Executive", "org": "SANBI"}, {"service": "B-BBEE Consulting & Training", "quote": "If you want to grow as an individual; if you want to grow as a team; and if you want your business to grow, I recommend GoldOurs!", "role": "Director", "org": "Jade-Sky Project Management (Pty) Ltd"}, {"service": "B-BBEE Consulting & Training", "quote": "Growth! Taking up the entrepreneur coaching program will grow your self-awareness, thinking ability, and leadership capability. It helped me focus on the highest priorities for lasting benefits of my business and my clients. Try it!", "role": "CEO & Founder", "org": "Changing Your Business Through Theatre (CYBTT) (Pty) Ltd"}];
  const quoteEl = $('#profile-quote-text');
  if (quoteEl) {
    let current = 0;
    const render = () => {
      const item = profileQuotes[current];
      quoteEl.textContent = '“' + item.quote + '”';
      $('#profile-quote-service').textContent = item.service;
      $('#profile-quote-org').textContent = item.org;
      $('#profile-quote-role').textContent = item.role;
      $('#profile-quote-counter').textContent = `${current + 1} / ${profileQuotes.length}`;
    };
    $('#profile-quote-prev')?.addEventListener('click', () => {current = (current + profileQuotes.length - 1) % profileQuotes.length;render();});
    $('#profile-quote-next')?.addEventListener('click', () => {current = (current + 1) % profileQuotes.length;render();});
    render();
  }
})();
