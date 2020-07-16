import React, { useState, useEffect } from "react";
import resources from "./resources";
import styles from "./styles.module.css";
function Resources(props) {
  return (
    <>
      <h1 className="title" style={{ margin: 0 }}>
        Resources Available
      </h1>
      <ul>
        {resources.map((resource) => (
          <li>
            <a href={resource.link}>{resource.text}</a>
          </li>
        ))}
      </ul>
    </>
  );
}

export default Resources;
