import React, { useState, useEffect } from "react";
import resources from "./resources";
import styles from "./styles.module.css";
import { Link, Fab } from "@material-ui/core";
import ArrowLeftIcon from "@material-ui/icons/ArrowLeft";
function Resources(props) {
  return (
    <>
      <h1 className="title" style={{ margin: 0 }}>
        Resources Available
      </h1>
      <div className={styles.box}>
        <ul>
          {resources.map((resource) => (
            <li>
              <Link href={resource.link}>{resource.text}</Link>
            </li>
          ))}
        </ul>
      </div>
      <Fab
        style={{ background: "#9206FF" }}
        aria-label="Go to previous page"
        size="medium"
        className="fab back-btn"
        onClick={() => {
          props.history.goBack();
        }}
      >
        <ArrowLeftIcon />
      </Fab>
    </>
  );
}

export default Resources;
